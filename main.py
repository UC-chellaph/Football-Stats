import pyodbc
import pandas as pd
from pandas import DataFrame  # Useful for dataframe style formatting. Not in use
import time
import jinja2  # Needed for formatting, not currently used
import Test1

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

connection_str = (
        'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

# --*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*----*--

currentMD = 24

connection = pyodbc.connect(connection_str)  # initialise connection

# execute the query and read to a dataframe in Python


del connection  # close the connection


# Define method for current fix list
def get_current_MatchDay():
    cnxn = pyodbc.connect(connection_str)
    query = ("Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored " +
             " as [Away], Away_Team as [Away Team] From dbo.Fixtures_PL_Full where [Round] = " + str(currentMD))
    data = pd.read_sql(query, cnxn)
    del cnxn
    return data


# data = get_current_MatchDay()
# print(data)


# Define method for next fixture list
def get_next_MatchDay():
    cnxn = pyodbc.connect(connection_str)
    query = ("Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored as [Away]," +
             " Away_Team as [Away Team] From dbo.Fixtures_PL_Full where [Round] = " + str(currentMD + 1))
    data = pd.read_sql(query, cnxn)
    del cnxn
    return data


def get_selected_MatchDay(matchday):
    cnxn = pyodbc.connect(connection_str)
    query = ("Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored as [Away]," +
             " Away_Team as [Away Team] From dbo.Fixtures_PL_Full where [Round] = " + str(matchday))
    data = pd.read_sql(query, cnxn)
    del cnxn
    return data


# nextWeek = get_next_MatchDay()
# print(nextWeek)
#
# matchDay = input('What Matchday would you like to get?: ')
# selectedMatchDay = get_selected_MatchDay(matchDay)
# print(selectedMatchDay)


def get_standings(league_id):
    cnxn = pyodbc.connect(connection_str)
    query = ("SELECT [team_short_name] as [Team Name],[points] as [Points],[match_played] as [Played],[won] as [Won]," +
             "[draw] as [Drawn],[lost] as [Lost] ,[goal_diff] as [Goal Diff] ,[goals_scored] as [Goals For] ,[goals_against] as" +
             " [Goals Against] FROM [dbo].[Standings_PL] where league_id = " + str(league_id))
    data = pd.read_sql(query, cnxn)
    del cnxn
    return data


# standings = get_standings(1)
# print(standings)


def get_team_fix(team_name):
    cnxn = pyodbc.connect(connection_str)
    query = (
            "Select Date, Home_team as [Home Team], Home_Goals_Scored as [Home], Away_Goals_Scored as [Away], Away_Team as [Away Team]" +
            " From dbo.Fixtures_PL_Full where Home_team = '" + str(team_name) + "' or Away_Team = '" + str(
        team_name) + "'")
    data = pd.read_sql(query, cnxn)
    del cnxn
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
#             ("SELECT [points] FROM [dbo].[Standings_PL] where team_full_name = '" + team_official_name + "'"), cnxn))
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


"Hi"

while 1:
    userInput = input('Hello! What would you like to do today?\n')
    validCommands = ' Fixtures Schedule Results Standings Team Info Table Get Help'
    helpCommand = "Hi! Welcome to this program. \nHere are some valid commands: \n" \
                  "Fixtures : Get Fixtures or results for a specific matchday or team \n" \
                  "Schedule : Same as above\n" \
                  "Next Week : Get Next Week's Fixtures\n" \
                  "Results : Get This Week's Results or Fixtures\n" \
                  "Standings : View the current table\n" \
                  "Team Info : Get Info about a team (Currently Unavailable)\n" \
                  "Help : This Command\n" \
                  "Team List: Full list of acceptable teams with spellings\n" \
                  "Credits : View Credits for this Project\n" \
                  "Quit : Close the Program"

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
                   'Insert Research Links here'

    if userInput.lower() == 'help' or userInput.lower() == 'get help':
        print(helpCommand)
        continue
    elif userInput.lower() == 'next week':
        print(get_next_MatchDay())

        response = input("Would You like to do something else? (type quit to quit) ")
        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'quit' or userInput.lower() == 'exit':
        break

    elif userInput.lower() == 'results' or userInput.lower() == 'scores':
        print(get_current_MatchDay())

        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'standings' or userInput.lower() == 'table':
        print(get_standings(1))

        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'team info':
        print("I'm sorry, this command is currently unavailable due to formatting errors in the code. "
              "It will be fixed in a future patch")

        response = input("Would You like to do something else? (type quit to quit) ")

        if response.lower() == 'y':
            continue
        elif response.lower() == 'quit' or response.lower() == 'exit':
            break

    elif userInput.lower() == 'team list':
        print(teamList)
        continue

    elif userInput.lower() == 'credit' or userInput.lower() == 'credits':
        print(creditString)
        continue

    elif userInput.lower() == 'fixtures' or userInput.lower() == 'schedule' or userInput.lower() == 'fix':
        matchdayOrTeam = input("Please enter a matchday or a team: ")

        if matchdayOrTeam.lower() == 'arsenal' or matchdayOrTeam.lower() == 'arsenal FC':
            team = 'Arsenal FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'aston villa' or matchdayOrTeam.lower() == 'aston villa fc' or matchdayOrTeam.lower() == 'villa':
            print(get_team_fix('Aston Villa FC'))
        elif matchdayOrTeam.lower() == 'brighton and hove albion' or matchdayOrTeam.lower() == 'brighton' or matchdayOrTeam.lower() == 'brighton & hove' or matchdayOrTeam.lower() == 'brighton and hove':
            team = 'Brighton & Hove Albion FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'chelsea' or matchdayOrTeam.lower() == 'chelsea fc':
            team = 'Chelsea FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'burnley' or matchdayOrTeam.lower() == 'burnley fc':
            team = 'Burnley FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'crystal palace' or matchdayOrTeam.lower() == 'palace' or matchdayOrTeam.lower() == 'cpfc':
            team = 'Crystal Palace FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'everton' or matchdayOrTeam.lower() == 'everton fc':
            team = 'Everton FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'fulham' or matchdayOrTeam.lower() == 'fulham fc':
            team = 'Fulham FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'leeds' or matchdayOrTeam.lower() == 'leeds united' or matchdayOrTeam.lower() == 'lufc':
            team = 'Leeds United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'liverpool fc' or matchdayOrTeam.lower() == 'liverpool':
            team = 'Liverpool FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'man city' or matchdayOrTeam.lower() == 'manchester city' or matchdayOrTeam.lower() == 'mcfc':
            team = 'Manchester City FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'man united' or matchdayOrTeam.lower() == 'manu' or matchdayOrTeam.lower() == 'man u' or matchdayOrTeam.lower() == 'manchester united' or matchdayOrTeam.lower() == 'mufc' or matchdayOrTeam.lower() == 'united' or matchdayOrTeam.lower() == 'manchester united fc':
            team = 'Manchester United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'newcastle' or matchdayOrTeam.lower() == 'newcastle united fc' or matchdayOrTeam.lower() == 'newcastle united':
            team = 'Newcastle United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'sheffield' or matchdayOrTeam.lower() == 'sheffield united':
            team = 'Sheffield United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'southampton' or matchdayOrTeam.lower() == 'southampton fc':
            team = 'Southampton FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'tottenham fc' or matchdayOrTeam.lower() == 'tottenham hotspur' or matchdayOrTeam.lower() == 'thfc' or matchdayOrTeam.lower() == 'spurs' or matchdayOrTeam.lower() == 'spurs fc' or matchdayOrTeam.lower() == 'tottenham' or matchdayOrTeam.lower() == 'best team in london':
            team = 'Tottenham Hotspur FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'west brom' or matchdayOrTeam.lower() == 'west bromwich' or matchdayOrTeam.lower() == 'west bromwich albion' or matchdayOrTeam.lower() == 'wbafc':
            team = 'West Bromwich Albion FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'west ham' or matchdayOrTeam.lower() == 'west ham united' or matchdayOrTeam.lower() == 'west ham united fc' or matchdayOrTeam.lower() == 'whufc':
            team = 'West Ham United FC'
            print(get_team_fix(team))
        elif matchdayOrTeam.lower() == 'wolves' or matchdayOrTeam.lower() == 'wolverhampton wanderers FC' or matchdayOrTeam.lower() == 'wolverhampton Wanderers':
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
