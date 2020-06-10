# Title     : TODO
# Objective : TODO
# Created by: sbbfti
# Created on: 10/06/2020

library(ggplot2)

getwd()

df <- read.table("./data/df_cozie.csv", header = TRUE, sep=",")
#names(df) <- c('thermal', 'met', 'userid', 'experimentid', 'responseSpeed')

# Basic box plot
p0 <- ggplot(df, aes(x=userid, y=responseSpeed)) +
  geom_boxplot()

# compute lower and upper whiskers
ylim1 <- boxplot.stats(df$responseSpeed)$stats[c(1, 5)]

# scale y limits based on ylim1
p1 <- p0 + coord_cartesian(ylim = ylim1*3)

p1

ggsave("./manuscript/src/figures/plot_r.png", width = 3, height = 1)