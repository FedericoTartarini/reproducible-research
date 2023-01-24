import matplotlib.pyplot as plt
import seaborn as sns

import os

sns.set_theme(style="white")


fig_dir = os.path.join(os.getcwd(), "manuscript", "src", "figures")
tbl_dir = os.path.join(os.getcwd(), "manuscript", "src", "tables")
data_dir = os.path.join(os.getcwd(), "manuscript", "src")


def save_var_latex(key, value):
    import csv

    dict_var = {}

    file_path = os.path.join(data_dir, "mydata.dat")

    try:
        with open(file_path, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                dict_var[row[0]] = row[1]
    except FileNotFoundError:
        pass

    dict_var[key] = value

    with open(file_path, "w") as f:
        for key in dict_var.keys():
            f.write(f"{key},{dict_var[key]}\n")


df = sns.load_dataset("penguins")

df = df[df.island == "Torgersen"]

save_var_latex(
    "n_penguins",
    df.shape[0],
)

f, ax = plt.subplots(constrained_layout=True, figsize=(3.5, 3))
sns.kdeplot(data=df, x="bill_length_mm", y="body_mass_g", hue="sex")
plt.savefig(os.path.join(fig_dir, "penguins_distribution.png"), dpi=300)
plt.show()

df.groupby(["sex"])["body_mass_g"].describe()[["count", "max", "min"]].round(
    2
).to_latex(
    os.path.join(tbl_dir, "penguins_sex.tex"),
    caption="Differences in penguins",
    label="tab:features",
    escape=False,
    column_format="lcccccccccc",
    index=True,
)
