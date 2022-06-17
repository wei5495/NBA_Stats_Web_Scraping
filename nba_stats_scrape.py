from bs4 import BeautifulSoup
import requests

url = 'https://www.pararius.com/apartments/amsterdam?ac=1'
page = requests.get(url)
soup = BeautifulSoup(page.content)
boxscore = soup.find('table', id='advanced_stats')

from csv import writer
# We have to define the mode also. if it is read only, then the mode should be r
with open('nba_advanced_stats.csv','w', encoding='utf8', newline='') as f:
    
    thewriter = writer(f)
    header = ['player_name', 'team', 'pos', 'age', 'game_played', 'minutes_played', 'per', 'true_s_perc', 'Three_Att_r', 'FTr', 'ORB_perc',
            'DRB_perc', 'TRB_perc', 'AST_perc', 'STL_perc', 'BLK_perc', 'TOV_perc', 'USG_perc', 'offensive_ws', 'defensive_ws', 'ws', 'ws_per_48', 
            'offensive_plus_minus','defensive_plus_minus', 'plus_minus', 'vorp']
    thewriter.writerow(header)

    for record in boxscore.find_all('tbody'):
        rows = record.find_all('tr',class_='full_table')
        # print(rows)
        for row in rows:
            player_name = row.find_all('a')[0].text
            team = row.find_all('td', class_ = 'left')[1].text
            position = row.find('td', class_= 'center').text
            age = row.find_all('td', class_= 'right')[0].text
            game_played = row.find_all('td', class_= 'right')[1].text
            minutes_played = row.find_all('td', class_= 'right')[2].text
            per = row.find_all('td', class_= 'right')[3].text
            true_s_perc = row.find_all('td', class_= 'right')[4].text
            Three_Att_r = row.find_all('td', class_= 'right')[5].text
            FTr = row.find_all('td', class_= 'right')[6].text
            ORB_perc = row.find_all('td', class_= 'right')[7].text
            DRB_perc = row.find_all('td', class_= 'right')[8].text
            TRB_perc = row.find_all('td', class_= 'right')[9].text
            AST_perc = row.find_all('td', class_= 'right')[10].text
            STL_perc = row.find_all('td', class_= 'right')[11].text
            BLK_perc = row.find_all('td', class_= 'right')[12].text
            TOV_perc = row.find_all('td', class_= 'right')[13].text
            USG_perc = row.find_all('td', class_= 'right')[14].text
            offensive_ws = row.find_all('td', class_= 'right')[16].text
            defensive_ws = row.find_all('td', class_= 'right')[17].text
            ws = row.find_all('td', class_= 'right')[18].text
            ws_per_48 = row.find_all('td', class_= 'right')[19].text
            offensive_plus_minus = row.find_all('td', class_= 'right')[21].text
            defensive_plus_minus = row.find_all('td', class_= 'right')[22].text
            plus_minus = row.find_all('td', class_= 'right')[23].text
            vorp = row.find_all('td', class_= 'right')[24].text

            info = [player_name, team, position, age, game_played, minutes_played, per, true_s_perc, Three_Att_r, FTr, ORB_perc,
            DRB_perc, TRB_perc, AST_perc, STL_perc, BLK_perc, TOV_perc, USG_perc, offensive_ws, defensive_ws, ws, ws_per_48, offensive_plus_minus,
            defensive_plus_minus, plus_minus, vorp]

            thewriter.writerow(info)