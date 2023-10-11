from bs4 import BeautifulSoup as bs4
import requests


urls_sess = 'https://en.wikipedia.org/wiki/Game_of_Thrones#Copyright_infringement'
response_sess = requests.get(urls_sess)
content = bs4(response_sess.text, 'html.parser')

episode = []

game_of_tronse_table = content.find_all(
    'table', class_='wikitable plainrowheaders')
# with open('game_of_tronse.html', 'w') as file:
#     file.write(str(game_of_tronse_table))

for table in game_of_tronse_table:
    header = []
    row = table.find_all('tr')
    
    for headerss in table.find('tr').find_all('th'):
        headerss.append(header.txt)
        
        # pass
        # with open('ths.html', 'a') as file:
        #     file.write(str(headerss)+ '\n')
        
    for row in table.find_all('tr')[1:9]:
        values = []
        for col in row.find_all(['th', 'td']):
            values.append(col.txt)
            
            # with open('values.html', 'a') as file:
            #     file.write(str(col) + '\n')
            
        if values:
            episode_dict = {header[i]: values[i]for i in range(len(values))}
            episode.append(episode_dict)
            
for ep in episode:
    with open('game_of_tronse.txt', 'a') as file:
        file.write(list(ep) + '\n')