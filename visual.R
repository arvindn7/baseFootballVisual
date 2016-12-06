library(ggplot2)

completedResults <- read.csv("/Users/arvindn/bin/FinishedFixtures.csv", header = T)
p <- ggplot(data = completedResults, aes(x=date, ReturnOn100QuidBet))
p + xlab("Fixture Date") + ylab("Return on 100 pound bet") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + geom_col()
