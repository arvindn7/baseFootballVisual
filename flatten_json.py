import csv, json, sys

def hasUnitedWon(homeTeamIn, awayTeamIn, homeGoalsIn, awayGoalsIn):
    return (
        (homeTeamIn == "Manchester United FC" and homeGoalsIn > awayGoalsIn) or
        (awayTeamIn == "Manchester United FC" and awayGoalsIn > homeGoalsIn)
    )

def numberOfUnitedGoals(homeTeamIn, homeGoalsIn, awayGoalsIn):
    return homeGoalsIn if homeTeamIn == "Manchester United FC" else awayGoalsIn

def returnOnBet(winFlag, winProbability):
    return bettingAmount * winProbability if winFlag else -1 * bettingAmount

input = open("/Users/arvindn/bin/MUFixtures.json")
data = json.load(input)
input.close()

output = csv.writer(open("/Users/arvindn/bin/MUFixtures.csv","wb"))

output.writerow(["id","date","status","homeTeam", "awayTeam", "goalsHomeTeam", "goalsAwayTeam", "oddsHomeWin","oddsAwayWin","oddsDraw","probHomeWin","probAwayWin","probDraw","bettingOverRound","UnitedWin", "UnitedGoals", "ReturnOn100QuidBet"])

fixtures = data['fixtures']

bettingAmount = 100

for row in fixtures:
    odds = row[unicode("odds")]
    # Initializing odds
    homeWinOdds = 0
    awayWinOdds = 0
    drawOdds = 0
    probHomeWin = 0
    probAwayWin = 0
    probDraw = 0
    totalProb = 0
    if odds is not None:
        homeWinOdds = odds[unicode("homeWin")]
        awayWinOdds = odds[unicode("awayWin")]
        drawOdds = odds[unicode("draw")]
        probHomeWin = round(100 / float(homeWinOdds), 2)
        probAwayWin = round(100 / float(awayWinOdds), 2)
        probDraw = round(100 / float(drawOdds), 2)
        totalProb = probHomeWin + probAwayWin + probDraw

    result = row[unicode("result")]
    homeGoals = 0
    awayGoals = 0
    if result is not None:
        homeGoals = result[unicode("goalsHomeTeam")]
        awayGoals = result[unicode("goalsAwayTeam")]

    unitedWin = hasUnitedWon(row[unicode("homeTeamName")], row[unicode("awayTeamName")], homeGoals, awayGoals)

    #Write row
    output.writerow([
        row[unicode("id")],
        row[unicode("date")],
        row[unicode("status")],
        row[unicode("homeTeamName")],
        row[unicode("awayTeamName")],
        homeGoals,
        awayGoals,
        homeWinOdds,
        awayWinOdds,
        drawOdds,
        probHomeWin,
        probAwayWin,
        probDraw,
        totalProb - 100,
        unitedWin,
        numberOfUnitedGoals(row[unicode("homeTeamName")], homeGoals, awayGoals),
        returnOnBet(unitedWin, homeWinOdds)
    ])

