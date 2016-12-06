library(ggplot2)

completedResults <- read.csv("/Users/arvindn/bin/FinishedFixtures.csv", header = T)
p <- ggplot(data = completedResults, aes(x=date, ReturnOn100QuidBet))
p + xlab("Fixture Date") + 
  ylab("Return on Bet") + 
  labs(title = "Betting on Manchester United", subtitle = "What if you bet 100 Pounds every game?") + 
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) + 
  geom_col()

  