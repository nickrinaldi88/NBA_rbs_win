import requests
from bs4 import BeautifulSoup
import re
import time
import pprint

from requests.models import guess_filename

main_endpoint = 'https://www.basketball-reference.com'

oct_response = requests.get(
    'https://www.basketball-reference.com/leagues/NBA_2022_games.html')
nov_response = requests.get(
    'https://www.basketball-reference.com/leagues/NBA_2022_games-november.html')

oct_response = oct_response.text
nov_response = nov_response.text

pattern = re.compile(r'Box Score')

oct_soup = BeautifulSoup(oct_response, 'html.parser')
nov_soup = BeautifulSoup(nov_response, 'html.parser')
soups = [oct_soup.find_all('a', text=pattern),
         nov_soup.find_all('a', text=pattern)]


# print(soup.title)

score = [box_score['href'] for soup in soups for box_score in soup]

winner_rbs = 0
winner_norbs = 0

# print(main_endpoint + score[0])

games = {}

teams = []
game_score = []


game_resp = requests.get(main_endpoint + score[0]).text
game_soup = BeautifulSoup(game_resp, 'html.parser')
for team in game_soup.find_all('a', attrs={'itemprop': 'name'}):
    teams.append(team.text)
for elem in game_soup.find_all('div', attrs={'class': 'score'}):
    game_score.append(elem.text)

team_totals = game_soup.find_all('tr', attrs={'data-row': True})

print(team_totals)

# for item in team_totals:
#     child = item.findChildren('')


print(teams)
print(game_score)

# print(type(game_soup.find_all('div', attrs={'id': 'all_line_score'})))

# for game in score:
#     game_resp = requests.get(main_endpoint + game).text
#     game_soup = BeautifulSoup(game_resp, 'html.parser')
#     for page in game_soup.find_all('td', data_point='T'):
#         print(page)
#         break

# winner = find_winner(game_soup)
# rbs_leader = find_rbs_leader(game_soup)
# if winner = rbs_leader:
#     winner_rbs +=1
# else:
#     winner_norbs += 1


def find_winner():
    pass

    # table id = line_score
    #       tr, th data-stat = T - text

    # take in page
    # on page, find line score table


def find_rbs_leader():
    pass

    # score.append(box_score)

    # print(len(score))

    # Fetch game logs
    # check rebounding numbers

    # bar chart
