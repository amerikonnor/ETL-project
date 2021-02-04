# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
##imports

from bs4 import BeautifulSoup
import requests
import pandas as pd 

# %%
##team name
##need to load the csv, put the name column into a list, and then loop literally the rest of the code lol

team_name = 'Arizona Cardinals'

team_name_for = team_name.lower().replace(' ','-')
team_name_for


# %%

## setting the url and getting the html
url = "https://www.nfl.com/teams/" + team_name_for + "/stats"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')


# %%

## grabs the list and puts all the list items into an array
result = soup.find('ul', class_="nfl-o-team-h2h-stats__list")

stat_list = result.find_all('li')

#stat_list


# %%

## empty arrays to hold the data
home_stats = []
titles = []
opponent_stats = []

#loop through each list item
for stat in stat_list:

    #getting the home team stat
    home_tag = stat.find('div', class_='nfl-o-team-h2h-stats__value')
    home = home_tag.text.strip()

    home_stats.append(home)


## getting the stat title
    title_block = stat.find('div', class_='nfl-o-team-h2h-stats__label')
    title = title_block.span.text

    titles.append(title)

## getting the opponents stat
    opponents = home_tag.find_next('div',class_='nfl-o-team-h2h-stats__value').text.strip()
    
    opponent_stats.append(opponents)


# %%
## in jupyter this found the indexes that needed the title changed. easier to do it here that in the dataframe
##titles.index('FIRST DOWNS'), titles.index('OFFENSE'), titles.index('RUSHING'), titles.index('PASSING'), titles.index('TOUCHDOWNS')


# %%

## adding the rest of the the details
titles[1] = 'FIRST DOWNS (Rushing - Passing - By Penalty)'
titles[5] = 'OFFENSE (Plays - Average Yards)'
titles[7] = 'RUSHING (Plays - Average Yards)'
titles[9] = 'PASSING (Comp - Att - Int - Avg)'
titles[12] = 'TOUCHDOWNS (Rushing - Passing - Returns - Defensive)'


# %%

## writng it all to a dataframe
cardinals_df = pd.DataFrame({'home':home_stats,'title':titles,'opponent':opponent_stats})
#cardinals_df.head()


# %%
##write it to a csv
cardinals_df.to_csv('team_stats/' + team_name_for)


# %%



