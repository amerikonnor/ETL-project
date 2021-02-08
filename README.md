# ETL-project Proposal
-	Data Sources
-	Data Cleanup
-	Data Analysis

Data Sources
1.	NFL team stats from https://www.nfl.com/stats/team-stats/
2.	NFL teams looked up and then typed into excel, saved as csv
3.	https://www.profootballnetwork.com/nfl-power-rankings-end-of-regular-season-week-17-2020/

      
Data Cleaning 

Data was extracted for NFL teams were aggregated for each team and their stats into a data base by looping by team and individual players in a csv file. Some of the stats used hyphens as joiners, but they were read as new line characters, so we decided to use string replace method instead, so we could store each team stats table in its own csv file.
Since all our data was based on the NFL teams; we decided to use a relational database. This let us store the team names in a table with a 'team_id', and then have a column 'team_id' in the rest of our tables to reference this instead of storing the team names every time.  Additionally, our database has a team’s table that contains the columns 'team_id' and 'team_name'. The team_id is how we then refer to the team in the other tables.

After converting the data to a csv, in a different jupyter file the csv was pulled. The team_id column was made by sorting the table by team name alphabetically, then making an index and incrementing by one. From here the team name was dropped, leaving team_id, ranking, and record. We then had to create good column names that are effectively used in SQL and rewrite our jupyter notebook to be able to use these column names instead.

The final tables or collections that were used in the production of this database are:

In order to aggregate every teams’ stats into one database, we first looped through every team’s individual csv file and pulled either the home or opponent column for the_all_stats or allowed_all_stats tables, respectively. These were then appended together using pandas. Next, we added the team_id column to the dataframe. 

Since our data always stayed in the same order as our teams csv, we did this just by adding one to the index. The last step of cleaning this data was to reorder the columns to get the team_id first. Finally, the dataframes were written to csv files.
The all_stats table contains the stats for every team from nfl.com. Some examples of the stats are first downs, touchdowns, passing yards, etc.
The allowed_all_stats tables contains the same kind of data as all_stats, but it also contains data for how many first downs, touchdowns, passing yards, etc., that each team allowed.

Rankings

The data for rankings was pretty clean, we had to gather each line from the html which had team, record, and rank, then split them using the .split() function. The Philidelphia Eagles ranking didn't work right because of a typo, but since it was the only one that was broken we just manually wrote in the info for it. 
The pro_fb_net_rankings table has the rankings from ProFootballNetwork, as well as each team's record. This could be further cleaned by adding the team records somewhere more central to the database.

Possibilities for Analysis:  

Developers can use this data in many ways. The nfl_stats_rankings table is an example of how the data can be used. the jupyter notebook file stat_based_rankings.ipynb uses the all_stats data to calculate a ranking for each team.

Developers could use this data to identify how much time during the game each team had the ball- average possession time vs yards or throwing touchdowns. This would show  which offense moved the fastest.

Data could be used to make comparisons of number of offensive plays vs touch downs between teams.
Additionally, data can help make projections about certain teams based on this data for upcoming season. Identify teams who may use a "bend not break defense" – may give up a ton of yards but not a lot of points.

Please add Schemata here:


Team members:
Britney Hopkins, Ryan Hathaway, Jet-Lania Simpson, Connor Mackensie, and Marisabel Matta-Hyams
