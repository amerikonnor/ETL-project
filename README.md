# ETL-project
Data Sources
1. NFL teams looked up and then typed into excel, saved as csv
2. NFL team stats from NFL.com/team-name/stats
    
    
    
Data Cleaning 

1. NFL teams

We needed to make sure that there was a 'team_id' column, and called the column with the teams 'team_name'.

2. Stats

There were a lot of new line characters at the beginning and end of some stats - had to strip these.
Some stats used hypens, but these were read as new line characters so we had to use the string replace method on these.
 We then stored each teams stat table in its own csv file.
        
 In order to aggregate every teams stats into one database, we first looped through every teams individual csv file and pulled either the home or opponent column for the all_stats or allowed_all_stats tables, respectively. These were then appended together using pandas. Next, we added the team_id column to the dataframe. Since our data always stayed in the same order as our teams csv, we did this just by adding one to the index. The last step of cleaning this data was to reorder the columns to get the team_id first. Finally, the dataframes were written to csv files.

We then had to create good column names that are usable in SQL and rewrite our jupyter notebook to use these column names instead.
        
        
Database

Since all of our data was based on the NFL teams; we decided to use a relational database. This let us store the team names in a table with a 'team_id', and then have a column 'team_id' in the rest of our tables to reference this instead of storing the team names every time.
