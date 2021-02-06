
##imports

from bs4 import BeautifulSoup
import requests
import pandas as pd 

def scraper(team_name):

    team_name_for = team_name.lower().replace(' ','-')
    team_name_for


    ## setting the url and getting the html
    url = "https://www.nfl.com/teams/" + team_name_for + "/stats"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')


    ## grabs the list and puts all the list items into an array
    result = soup.find('ul', class_="nfl-o-team-h2h-stats__list")

    stat_list = result.find_all('li')

    #stat_list


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


    # getting the stat title
        title_block = stat.find('div', class_='nfl-o-team-h2h-stats__label')
        title = title_block.span.text

        titles.append(title)

    # getting the opponents stat
        opponents = home_tag.find_next('div',class_='nfl-o-team-h2h-stats__value').text.strip()
    
        opponent_stats.append(opponents)


    #changing nan in home turnover ratio to 0, setting opponent turnover ratio to opposite sign
    if home_stats[15] == '':
        home_stats[15] = 0
        opponent_stats[15] = 0
    else:
        opponent_stats[15] = home_stats[15]

    if str(opponent_stats[15])[0] == '+':
        opponent_stats[15] = opponent_stats[-1].replace('+', '-')
    elif str(opponent_stats[15])[0] == '-':
        opponent_stats[15] = opponent_stats[-1].replace('-','+')


    ## in jupyter this found the indexes that needed the title changed. easier to do it here that in the dataframe
    ##titles.index('FIRST DOWNS'), titles.index('OFFENSE'), titles.index('RUSHING'), titles.index('PASSING'), titles.index('TOUCHDOWNS')


    ## adding the rest of the the details
    titles[1] = 'FIRST DOWNS (Rushing - Passing - By Penalty)'
    titles[5] = 'OFFENSE (Plays - Average Yards)'
    titles[7] = 'RUSHING (Plays - Average Yards)'
    titles[9] = 'PASSING (Comp - Att - Int - Avg)'
    titles[13] = 'TOUCHDOWNS (Rushing - Passing - Returns - Defensive)'


    ## writng it all to a dataframe
    df = pd.DataFrame({'home':home_stats,'title':titles,'opponent':opponent_stats})
    #df.head()

    # remove all the internal new line characters, format dashes and slashes
    for i in range(0,len(df)):
        stat = str(df.iloc[i,0])
        stat = stat.replace(' ', '')
        stat = stat.replace('/', ' / ')
        stat = stat.replace('\n',' - ')
        df.iloc[i,0] = stat

        stat = str(df.iloc[i,2])
        stat = stat.replace(' ', '')
        stat = stat.replace('/', ' / ')
        stat = stat.replace('\n',' - ')
        df.iloc[i,2] = stat

    df = df[['title', 'home', 'opponent']]

    ##write it to a csv
    filepath = 'resources/team_stats/' + team_name_for + '.csv'
    df.to_csv(filepath, index=False)






