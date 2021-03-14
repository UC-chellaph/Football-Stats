import pyodbc
import pandas as pd
import time
from datetime import date
import requests
from bs4 import BeautifulSoup as bs

# Local Connection code below

# connection_str = ("Driver={SQL Server Native Client 11.0};"
#             "Server=LAPTOP-VKN8AU2E\SQLEXPRESS;"
#             "Database=Football_Stats;"
#             "Trusted_Connection=yes;")

# Azure Connection code below

print("Loading...")

reader = open("Test1", "r")

username = 'Chellaph'
password = reader.readline()
server = 'it3038c-coursework.database.windows.net'
driver = '{ODBC Driver 17 for SQL Server}'
database = 'Football_Stats'

reader.close()

# Connection String 1 below

connection_str = (
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# If the Above doesn't work, comment it out and use the connection string below.


# connection_str = (
# 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:it3038c-coursework.database.windows.net,1433;Database=Football_Stats;Uid=Chellaph;Pwd='+password+';Encrypt=yes;'
# )

# --*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*--

today = date.today()

# Block of code to set current MatchDay

GW1 = date(2020, 9, 11)
GW2 = date(2020, 9, 18)
GW3 = date(2020, 9, 25)
GW4 = date(2020, 10, 2)
GW5 = date(2020, 10, 15)
GW6 = date(2020, 10, 22)
GW7 = date(2020, 10, 29)
GW8 = date(2020, 11, 5)
GW9 = date(2020, 11, 19)
GW10 = date(2020, 11, 26)
GW11 = date(2020, 12, 3)
GW12 = date(2020, 12, 10)
GW13 = date(2020, 12, 14)
GW14 = date(2020, 12, 17)
GW15 = date(2020, 12, 24)
GW16 = date(2020, 12, 28)
GW17 = date(2021, 1, 1)
GW18 = date(2021, 1, 11)
GW19 = date(2021, 1, 14)
GW20 = date(2021, 1, 25)
GW21 = date(2021, 1, 28)
GW22 = date(2021, 2, 1)
GW23 = date(2021, 2, 5)
GW24 = date(2021, 2, 11)
GW25 = date(2021, 2, 18)
GW26 = date(2021, 2, 25)
GW27 = date(2021, 3, 4)
GW28 = date(2021, 3, 11)
GW29 = date(2021, 3, 18)
GW30 = date(2021, 4, 1)
GW31 = date(2021, 4, 8)
GW32 = date(2021, 4, 15)
GW33 = date(2021, 4, 22)
GW34 = date(2021, 4, 29)
GW35 = date(2021, 5, 6)
GW36 = date(2021, 5, 10)
GW37 = date(2021, 5, 13)
GW38 = date(2021, 5, 21)

# Defining Current MD

currentMD = 1

if today < GW2:
    currentMD = 1
elif GW2 < today < GW3:
    currentMD = 2
elif GW3 < today < GW4:
    currentMD = 3
elif GW4 < today < GW5:
    currentMD = 4
elif GW5 < today < GW6:
    currentMD = 5
elif GW6 < today < GW7:
    currentMD = 6
elif GW7 < today < GW8:
    currentMD = 7
elif GW8 < today < GW9:
    currentMD = 8
elif GW9 < today < GW10:
    currentMD = 9
elif GW10 < today < GW11:
    currentMD = 10
elif GW11 < today < GW12:
    currentMD = 11
elif GW12 < today < GW13:
    currentMD = 12
elif GW13 < today < GW14:
    currentMD = 13
elif GW14 < today < GW15:
    currentMD = 14
elif GW15 < today < GW16:
    currentMD = 15
elif GW16 < today < GW17:
    currentMD = 16
elif GW17 < today < GW18:
    currentMD = 17
elif GW18 < today < GW19:
    currentMD = 18
elif GW19 < today < GW20:
    currentMD = 19
elif GW20 < today < GW21:
    currentMD = 20
elif GW21 < today < GW22:
    currentMD = 21
elif GW22 < today < GW23:
    currentMD = 22
elif GW23 < today < GW24:
    currentMD = 23
elif GW24 < today < GW25:
    currentMD = 24
elif GW25 < today < GW26:
    currentMD = 25
elif GW26 < today < GW27:
    currentMD = 26
elif GW27 < today < GW28:
    currentMD = 27
elif GW28 < today < GW29:
    currentMD = 28
elif GW29 < today < GW30:
    currentMD = 29
elif GW30 < today < GW31:
    currentMD = 30
elif GW31 < today < GW32:
    currentMD = 31
elif GW32 < today < GW33:
    currentMD = 32
elif GW33 < today < GW34:
    currentMD = 33
elif GW34 < today < GW35:
    currentMD = 34
elif GW35 < today < GW36:
    currentMD = 35
elif GW36 < today < GW37:
    currentMD = 36
elif GW37 < today < GW38:
    currentMD = 37
elif GW37 < today:
    currentMD = 38

print('Hello! \n')
print(
    "Today's date is " + str(today) + '. This means the current match week we are on is Match Week: ' + str(currentMD))

print("-------------------------------------------------------------------------------------------------")


def getAllCompResults(teamname):
    if teamname in arsenalAliases:
        team1name = 'Arsenal'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=142&comp_id=1'
    elif teamname in villaAliases:
        team1name = 'Aston Villa'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=154&comp_id=1'
    elif teamname in brightonAliases:
        team1name = 'Brighton'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=381&comp_id=1'
    elif teamname in chelseaAliases:
        team1name = 'Chelsea'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=536&comp_id=1'
    elif teamname in burnleyAliases:
        team1name = 'Burnley'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=435&comp_id=1'
    elif teamname in palaceAliases:
        team1name = 'Crystal Palace'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=646&comp_id=1'
    elif teamname in evertonAliases:
        team1name = 'Everton'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=942&comp_id=1'
    elif teamname in fulhamAliases:
        team1name = 'Fulham'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=1055&comp_id=1'
    elif teamname in leedsAliases:
        team1name = 'Leeds'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=1524&comp_id=1'
    elif teamname in leicesterAliases:
        team1name = 'Leicester'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=1527&comp_id=1'
    elif teamname in liverpoolAliases:
        team1name = 'Liverpool'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=1563&comp_id=1'
    elif teamname in cityAliases:
        team1name = 'Man City'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=1718&comp_id=1'
    elif teamname in unitedAliases:
        team1name = 'Man Utd'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=1724&comp_id=1'
    elif teamname in newcastleAliases:
        team1name = 'Newcastle'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=1823&comp_id=1'
    elif teamname in sheffieldAliases:
        team1name = 'Sheffield United'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=2328&comp_id=1'
    elif teamname in southamptonAliases:
        team1name = 'Southampton'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=2471&comp_id=1'
    elif teamname in spursAliases:
        team1name = 'Spurs'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=2590&comp_id=1'
    elif teamname in westBromAliases:
        team1name = 'West Brom'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=2744&comp_id=1'
    elif teamname in westHamAliases:
        team1name = 'West Ham'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=2802&comp_id=1'
    elif teamname in wolvesAliases:
        team1name = 'Wolves'
        link = 'https://www.soccerbase.com/teams/team.sd?team_id=2848&comp_id=1'
    else:
        print(
            "That is not a valid response. Please enter a valid team name "
            "Type Team List on the main screen for a full list of valid team names")
        return

    consolidated = []
    print('Acquiring live %s data...' % team1name)

    headers = ['Team', 'Competition', 'Home Team', 'Home Score', 'Away Team', 'Away Score', 'Date Keep']
    r = requests.get('%s&teamTabs=results' % link)
    soup = bs(r.content, 'html.parser')

    h_scores = [int(i.text) for i in soup.select('.score a em:first-child')]
    a_scores = [int(i.text) for i in soup.select('.score a em + em')]

    limit = len(a_scores)
    team1name = [team1name for i in soup.select('.tournament', limit=limit)]
    comps = [i.text for i in soup.select('.tournament a', limit=limit)]
    dates = [i.text for i in soup.select('.dateTime .hide', limit=limit)]
    h_teams = [i.text for i in soup.select('.homeTeam a', limit=limit)]
    a_teams = [i.text for i in soup.select('.awayTeam a', limit=limit)]

    df = pd.DataFrame(list(zip(team1name, comps, h_teams, h_scores, a_teams, a_scores, dates)),
                      columns=headers)
    consolidated.append(df)

    print(pd.concat(consolidated))


# Define method for current fix list
def get_current_MatchDay():
    connection = pyodbc.connect(connection_str)
    query = ("Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored " +
             " as [Away], Away_Team as [Away Team] From dbo.Fixtures_PL_Full where [Round] = " + str(currentMD))
    data = pd.read_sql(query, connection)
    del connection
    return data


# Define method for next fixture list
def get_next_MatchDay():
    connection = pyodbc.connect(connection_str)
    query = ("Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored as [Away]," +
             " Away_Team as [Away Team] From dbo.Fixtures_PL_Full where [Round] = " + str(currentMD + 1))
    data = pd.read_sql(query, connection)
    del connection
    return data


def get_selected_MatchDay(matchday):
    connection = pyodbc.connect(connection_str)
    query = ("Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored as [Away]," +
             " Away_Team as [Away Team] From dbo.Fixtures_PL_Full where [Round] = " + str(matchday))
    data = pd.read_sql(query, connection)
    del connection
    return data


def get_standings(league_id):
    connection = pyodbc.connect(connection_str)
    query = ("SELECT [team_short_name] as [Team Name],[points] as [Points],[match_played] as [Played],[won] as [Won]," +
             "[draw] as [Drawn],[lost] as [Lost] ,[goal_diff] as [Goal Diff] ,[goals_scored] as [Goals For] ,[goals_against] as" +
             " [Goals Against] FROM [dbo].[Standings_PL] where league_id = " + str(league_id))
    data = pd.read_sql(query, connection)
    del connection
    return data


def get_team_fix(team_name):
    connection = pyodbc.connect(connection_str)
    query = (
            "Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored as [Away], Away_Team as [Away Team]" +
            " From dbo.Fixtures_PL_Full where Home_team = '" + str(team_name) + "' or Away_Team = '" + str(
        team_name) + "'")
    data = pd.read_sql(query, connection)
    del connection
    return data


# Code below to retrieve team details. Partially works, but formatting issue - Adds index to display


# var1 = get_team_fix("Arsenal FC")
# print(var1)

# def get_team_info(team_official_name):
#     cnxn = pyodbc.connect(cnxn_str)
#
#     team_name = str(pd.read_sql(
#         ("SELECT [team_short_name] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"),
#         cnxn))
#     played = str(pd.read_sql(
#         ("SELECT [match_played] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"), cnxn))
#     won = str(pd.read_sql(
#         ("SELECT [won] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"), cnxn))
#     drawn = str(pd.read_sql(
#         ("SELECT [draw] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"), cnxn))
#     lost = str(pd.read_sql(
#         ("SELECT [lost] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"), cnxn))
#     goalsScored = str(pd.read_sql(
#         ("SELECT [goals_scored] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"), cnxn))
#     goalsConceded = str(pd.read_sql(
#         ("SELECT [goals_against] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"), cnxn))
#     points = str(pd.read_sql(
#             ("SELECT [points] FROM [dbo].[Standings_PL] where team_full_nam = '" + team_official_name + "'"), cnxn))
#
#     del cnxn
#
#     toPrint = ("You've chosen" + team_name.split('\n', 1)[1] + '\n' +
#                team_name.split('\n', 1)[1] + "'s official name is: " + team_official_name + '\n' +
#                "They have played " + played.split('\n', 1)[1] + " matches so far, of which they have won " + won.split('\n', 1)[1] + " and lost " + lost.split('\n', 1)[1] + '\n' +
#                "They have drawn " + drawn.split('\n', 1)[1] + " games, and have a total of " + points.split('\n', 1)[1] + " points." + '\n' +
#                "They have scored " + goalsScored.split('\n', 1)[1] + " so far, and have conceded " + goalsConceded.split('\n', 1)[1])
#     print(toPrint)
#     return team_name

# var2 = get_team_info('Arsenal FC')
# print(var2)


'-------------------------------'

# Defining Aliases list

arsenalAliases = ["arsenal", "arsenal fc", "gunners"]
villaAliases = ['aston villa', 'aston villa fc', 'villa', 'villains', 'avfc']
brightonAliases = ['brighton and hove albion', 'brighton', 'brighton & hove', 'brighton and hove', 'bhafc']
chelseaAliases = ['chelsea', 'chelsea fc', 'blues']
burnleyAliases = ['burnley', 'burley fc', 'clarets']
palaceAliases = ['palace', 'crystal palace', 'crystal palace fc', 'cpfc', 'eagles']
evertonAliases = ['everton', 'toffees', 'everton fc']
fulhamAliases = ['fulham', 'fulham fc']
leedsAliases = ['leeds', 'leeds united', 'leeds united fc', 'lufc']
leicesterAliases = ['leicester city', 'leicester city fc', 'lcfc', 'foxes', 'leicester']
liverpoolAliases = ['liverpool', 'liverpool fc', 'lfc', 'reds', 'kop']
cityAliases = ['city', 'mancity', 'man city', 'manchester city', 'manchester city fc', 'mcfc', 'cityzens']
unitedAliases = ['man united', 'manu', 'manchester united', 'manchester united fc', 'red devils', 'mufc']
newcastleAliases = ['newcastle', 'newcastle united', 'newcastle united', 'nufc']
sheffieldAliases = ['sheffield united', 'blades', 'sheffield united fc', 'sufc']
southamptonAliases = ['southampton', 'southampton fc', 'saints', 'soton']
spursAliases = ['tottenham fc', 'tottenham hotspur', 'thfc', 'spurs', 'spurs fc', 'lilywhites', 'tottenham',
                'best team in london']
westBromAliases = ['west bromwich albion', 'west bromwich albion fc', 'wbafc', 'baggies', 'west brom',
                   'west brom albion']
westHamAliases = ['west ham', 'west ham united', 'west ham united fc', 'west ham fc', 'whufc', 'hammers', 'irons']
wolvesAliases = ['wolverhampton wanderers fc', 'wolverhampton wanderers', 'wolves', 'wfc']

# Main Method

while 1:
    userInput = input('What would you like to do today?\n')
    validCommands = ' Fixtures Schedule Results Standings Team Info Table Get Help'
    helpCommand = "Hi! Welcome to this program. \nHere are some valid commands: \n" \
                  "Fixtures : Get Fixtures or results for a specific matchday or team \n" \
                  "Schedule : Same as above\n" \
                  "Next Week : Get Next Week's Fixtures\n" \
                  "Results : Get This Week's Results or Fixtures\n" \
                  "Standings : View the current table\n" \
                  "Team Info : Get Info about a team (Currently Unavailable)\n" \
                  "Full Fixtures : Get a Premier League team's results from all competitions (Retrieved live)\n" \
                  "Help : This Command\n" \
                  "Team List: Full list of acceptable teams with spellings\n" \
                  "Credits : View Credits for this Project\n" \
                  "Quit : Close the Program\n" \
                  "For more detailed information on each command, please read the ReadMe file at https://github.com/UC-chellaph/Football-Stats"

    teamList = "Here is a full list of Premier League teams:\n" \
               "Arsenal FC\n" \
               "Aston Villa FC\n" \
               "Brighton & Hove Albion FC\n" \
               "Burnley FC\n" \
               "Chelsea FC\n" \
               "Crystal Palace FC\n" \
               "Everton FC\n" \
               "Fulham FC\n" \
               "Leeds United FC\n" \
               "Leicester City FC\n" \
               "Liverpool FC\n" \
               "Manchester City FC\n" \
               "Manchester United FC\n" \
               "Newcastle United FC\n" \
               "Sheffield United FC\n" \
               "Southampton FC\n" \
               "Tottenham Hotspur FC\n" \
               "West Bromwich Albion FC\n" \
               "West Ham United FC\n" \
               "Wolverhampton Wanderers FC\n"

    creditString = 'This Application was made by Prateek Chellani as part of the IT3038C - Scripting Languages class\n' \
                   'The Idea for this project was inspired by a Github repo called ShellScore, by Jason Auger\n' \
                   'You can learn more about ShellScore here - \n' \
                   'While almost all of the code in this is original and not available anywhere else, here are some links I used to create this - \n' \
                   'How to use pyodbc to connect to SQL - https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15  and https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/\n' \
                   'Inserting data into Pandas Dataframes - https://docs.microsoft.com/en-us/sql/machine-learning/data-exploration/python-dataframe-sql-server?view=sql-server-ver15\n' \
                   'While the Database was created in SQLServer (Hosted on Azure) using SSMS, the intial list of fixtures was imported from this CSV:  https://footystats.org/download-stats-csv\n' \
                   'https://github.com/footballcsv/england was also useful for Premier League Fixtures\n' \
                   'A lot of the scraping help (And code) was taken from https://stackoverflow.com/questions/59024776/how-to-scrape-football-results-from-sofascore-using-python \n' \
                   'https://www.kdnuggets.com/2020/11/build-football-dataset-web-scraping.html and https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/ were also looked at for understanding web scraping \n' \
                   'Lastly, several other links, StackOverflow responses and Youtube tutorials were used to create this program\n' \
                   'For further clarification or queries, please reach out to me at prateekchellani@gmail.com\n\n'

    if userInput.lower() == 'help' or userInput.lower() == 'get help':
        print(helpCommand)
        continue
    elif userInput.lower() == 'next week':
        print(get_next_MatchDay())
        print("-------------------------------------------------------------------------------------------------")
        response = input("Would You like to do something else? (type quit to quit) ")
        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'quit' or userInput.lower() == 'exit':
        break

    elif userInput.lower() == 'results' or userInput.lower() == 'scores' or userInput.lower() == 'this week' or userInput.lower() == 'score':
        print(get_current_MatchDay())
        print("-------------------------------------------------------------------------------------------------")
        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'standings' or userInput.lower() == 'table':
        print(get_standings(1))
        print("-------------------------------------------------------------------------------------------------")
        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'team info':
        print("I'm sorry, this command is currently unavailable due to formatting errors in the code. "
              "It will be fixed in a future patch")
        print("-------------------------------------------------------------------------------------------------")
        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'team list':
        print(teamList)
        print("-------------------------------------------------------------------------------------------------")
        continue

    elif userInput.lower() == 'credit' or userInput.lower() == 'credits':
        print(creditString)
        print("-------------------------------------------------------------------------------------------------")
        continue

    elif userInput.lower() == 'allfix' or userInput.lower() == 'full fix' or userInput.lower() == 'full fixtures':
        teamName = input("Please enter a team: ")
        getAllCompResults(teamName.lower())
        print("-------------------------------------------------------------------------------------------------")
        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'fixtures' or userInput.lower() == 'schedule' or userInput.lower() == 'fix':
        matchdayOrTeam = input("Please enter a matchday or a team: ")

        if matchdayOrTeam.lower() in arsenalAliases:
            team = 'Arsenal FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in villaAliases:
            print(get_team_fix('Aston Villa FC'))
        elif matchdayOrTeam.lower() in brightonAliases:
            team = 'Brighton & Hove Albion FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in chelseaAliases:
            team = 'Chelsea FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in burnleyAliases:
            team = 'Burnley FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in palaceAliases:
            team = 'Crystal Palace FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in evertonAliases:
            team = 'Everton FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in fulhamAliases:
            team = 'Fulham FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in leedsAliases:
            team = 'Leeds United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in leicesterAliases:
            team = 'Leicester City FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in liverpoolAliases:
            team = 'Liverpool FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in cityAliases:
            team = 'Manchester City FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in unitedAliases:
            team = 'Manchester United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in newcastleAliases:
            team = 'Newcastle United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in sheffieldAliases:
            team = 'Sheffield United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in southamptonAliases:
            team = 'Southampton FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in spursAliases:
            team = 'Tottenham Hotspur FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in westBromAliases:
            team = 'West Bromwich Albion FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in westHamAliases:
            team = 'West Ham United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() in wolvesAliases:
            team = 'Wolverhampton Wanderers FC'
            print(get_team_fix(team))

        elif 5 == 5:
            try:
                matchDay = int(matchdayOrTeam)
                print(get_selected_MatchDay(matchDay))
            except ValueError:
                print(
                    "That is not a valid response. Please only enter a number between 1 and 38 or a valid team name "
                    "Type Team List on the main screen for a full list of valid team names")
                continue

        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break
    elif 5 == 5:
        print("I'm sorry, I don't understand that command. Please type 'help' to get a list of valid commands")
        continue

print("Have a great day!")
time.sleep(3)
