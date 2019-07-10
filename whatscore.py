import requests
from bs4 import BeautifulSoup

match_url = 'https://www.cricbuzz.com/cricket-match/live-scores'

res = requests.get(match_url)
soup = BeautifulSoup(res.text, 'html.parser')

scoreDiv = soup.find('div',{'class': 'cb-lv-scrs-col'})
additionalMessage = soup.find('div',{'class': 'cb-text-live'})

print(scoreDiv.text)
print(additionalMessage.text)

