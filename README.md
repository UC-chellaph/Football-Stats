# Football-Stats

This program was designed by Prateek Chellani during his time at the University of Cincinnati as part of a class project. It connects to an Azure database built in SQL Server and retrieves scores, results, fixtures and standings for the world's leading football league, the English Premier League

![alt text](https://imgur.com/5VljUXw.gif "Demo by Prateek Chellani")

*More Leagues to be added soon.*

 -----
 # Valid Commands and Aliases 

Type Help after loading into the Program for a list of valid commands, several of which have aliases as well. 

|**Valid Commands** | **Result**                                                   | **Aliases**                | **Version Added** |
|-------------------|--------------------------------------------------------------|----------------------------|-------------------|
|Fixtures           | Get Fixtures or results for a specific matchday or team      | Fix, Schedule              |     Version 1     |
|Next Week          | Get Next Week's Fixtures                                     |                            |     Version 1     |
|Results            | Get This Week's Results or Fixtures                          | Scores, Score, This Week   |     Version 1     |
|All Fixtures       | Get a team's results from all competitions - from SofaScore  | AllFix, Full Fix           |     Version 2     |
|Standings          | View the current table                                       | Table                      |     Version 1     |
|Team Info          | Get Info about a team (Currently Unavailable)                |                            |     Version 1     |
|Help               | Get this list of commands                                    | Get Help                   |     Version 1     |
|Team List          | Full list of acceptable teams with spellings                 |                            |     Version 1     |
|Credits            | View Credits for this Project                                | Credit                     |     Version 1     |
|Quit               | Close the Program                                            | Exit                       |     Version 1     |


 -----

# Supported Teams
All 20 teams registered in the English Premier League for the 2020-21 season valid inputs. Entering their official name (As displayed in team list) is preferred.
However, most popular abbreviations such as 'Spurs' for Tottenham Hotspur FC, or ManUtd for Manchester United FC are also accepted. 

 -----
 
# Features

- [X] All 20 Premier League Teams.
- [X] 380 league matches covered over 38 weeks.
- [X] Weekly score updates.
- [X] Automated Match day selection.
- [X] Multiple team and command aliases to include all popular nicknames and abbreviations
- [X] Detailed standings table with team summaries for goals scored, conceded, matches played, etc. 
- [X] Input Error handling.
- [X] Ability to perform multiple commands without having to restart the program. 
- [X] Compatible with Windows, Mac, CentOS Linux and Ubuntu
- [X] Results from all competitions, including the FA Cup, League Cup, and Continental Competitions
- [X] Live results retrieval from SofaScore.com - Only certain commands. 
- [ ] Premier League Logos - To be added in a future update
- [ ] Team Stats and recent form - To be added in a future update
- [ ] Live score retrieval using APIs/Web Scraping - Partially incorporated. 
- [ ] Individual Player Stats - No current incorporation plans
----


# Installation Instructions

1. Clone this Repository. Can be done through CLI or via Github Desktop. 
2. Ensure that you have Python installed. (pip install python on Windows, yum -y install python on CentOS)
3. Install the required imports and packages - pandas, datetime, pyodbc, requests, bs4 (BeautifulSoup). (pip install pyodbc/pandas/datetime/etc.)
   - Ensure that you install these in the correct folder (where you have installed Python, and intend to run the app from)
4. Install the ODBC Driver from https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15
   - Install the Microsoft ODBC Driver 17 for SQL Server and leave default settings. 
   - Open the installed program (OODBC Data Sources) and add the SQL Server driver from the list. Again, leave to default settings, and set name to Microsoft ODBC Driver 17 for SQL Server. Make sure to use SQL Server authentication rather than Windows Auth. 
   ![alt text](https://i.imgur.com/aHsI472.png "ODBC Settings")
5. With the configuration done, load up your script through Python. You can either browse the the directory where your main.py is located and open it in Python, or type python main.py into the CLI in the correct folder. 
   - I strongly recommend using Python2 rather than Python3.
6. And this one time set-up is now complete. Following this, you can launch the file as you normally would. 

 -----
# Troubleshooting

1. **I keep getting the following error - Data source name not found and no default driver specified**
   - Check your ODBC installations. Did you follow through all steps under step 4 of Installation instructions? Check your driver name. 
   - If this doesn't help, try changing the connection string in the Python Script. There is an alternate connection string provided and commented out. Use that. 
2. **I get the error 'Failed to import Pandas/Pyodbc/datetime/Requests/BS4**
   - Have you installed the required packages? Are the in the correct location?
   - If yes, and you still seem to be getting errors for pyodbc, try running the script in Python2 (This is the VEnv that packages install in by default)
3. **I keep getting the error - failed to authenticate user Chellaph**
   - Have you cloned all files from Github? Make sure there is a file called 'text'
4. **My python program automatically closes on opening**
   - Open it in a text editor via linux and check the error trace. 
5. **It doesn't recognize my commands**
   - Type help to get a valid list of commands, and use these. 
6. **The standings and Fixture tables show '....' instead of some scores.**
   - This is a known issue, due to the way Python formats it's output. The output should work normally on most computers, however if the screen size/console size is restricted, Python may replace data with '....' . One potential fix is to try running this in full screen mode, via the command prompt or a different CLI.
