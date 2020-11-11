import matplotlib.pyplot as plt
import pandas as pd
from influxdb import InfluxDBClient
import seaborn as sns
import matplotlib
import os


# from IPython.display import display, Markdown
# display(Markdown("Hello World!"))
# print("Hello World!")


def influx_to_df(query='SELECT * FROM "coziePublic"."autogen"."fitbit" where userid=\'test\''):
    import secret

    influx_cl = InfluxDBClient(host=secret.influx_db_host, port=8086,
                               username="heroku", password=secret.influx_db_psw,
                               database="spaces", ssl=True, verify_ssl=True)

    try:
        result = influx_cl.query(query)
        df = pd.DataFrame(result[result.keys()[0]])

        df.index = pd.to_datetime(df.time)
        df.index = df.index.tz_convert(timeZone)
        return df.drop(coKlumns=['time'])
    except IndexError:
        return pd.DataFrame()

# variables
experiment_id = 'dorn'
timeZone = 'Asia/Singapore'
start_date = pd.Timestamp(2020, 4, 10).value
fig_dir = os.path.join(os.getcwd(), 'manuscript', 'src', 'figures')
tbl_dir = os.path.join(os.getcwd(), 'manuscript', 'src', 'tables')
data_dir = os.path.join(os.getcwd(), 'data')
cozie_file = os.path.join(data_dir, 'df_cozie.csv')

try:
    df_cozie = influx_to_df(f'SELECT thermal, met, userid, experimentid, responseSpeed '
                            f'FROM "coziePublic"."autogen"."fitbit" '
                            f'where time > {start_date} '
                            f'and "experimentid" = \'{experiment_id}\' '
                            f'and "userid" != \'{"dorn16"}\''
                            f'and "userid" != \'{"dorn18"}\''
                            f'and "userid" != \'{"dorn17"}\'')
    df_cozie.to_csv(cozie_file, index=False)
except:
    df_cozie = pd.read_csv(cozie_file)

df_cozie.head()
df_cozie.index.max()

df_group_id = df_cozie.groupby(['userid'])['thermal'].count().reset_index()

fig = plt.figure(figsize=(7.2, 5))
sns.barplot(y="userid", x="thermal", data=df_group_id)
plt.show()

# matplotlib.use("pgf")
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })

fig = plt.figure(figsize=(2, 2))
sns.barplot(y="userid", x="thermal", data=df_group_id)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'bar-plot.pgf'))

fig = plt.figure(figsize=(3, 3))
sns.barplot(y="userid", x="thermal", data=df_group_id)
plt.tight_layout()
# plt.savefig(os.path.join(fig_dir, 'beamer-bar-plot.pgf'))
plt.savefig(os.path.join(fig_dir, 'bar-plot.png'), dpi=300)

fig = plt.figure(figsize=(3, 3))
sns.barplot(y="userid", x="thermal", data=df_group_id)
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'beamer-bar-plot.pgf'))
# plt.savefig(os.path.join(fig_dir, 'bar-plot.png'), dpi=300)

df_cozie.groupby(['userid'])['responseSpeed'].describe()

# df_describe = df_cozie.groupby(['userid'])['responseSpeed'].describe()
df_describe = df_cozie.groupby(['userid'])['responseSpeed'].describe().round(1).reset_index()
# df_describe['mean'] = [str(x) if x > 400 else str(x) + '*' for x in df_describe['mean']]
df_describe = df_describe[df_describe.columns[:4]]
with open(os.path.join(tbl_dir, 'tbl_resp_speed.tex'), 'w') as tf:
    tf.write(df_describe.to_latex(index=False))
