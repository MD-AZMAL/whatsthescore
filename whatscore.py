import requests
from bs4 import BeautifulSoup
import os
import subprocess as sp

match_url = 'https://www.cricbuzz.com/cricket-match/live-scores'

res = requests.get(match_url)
soup = BeautifulSoup(res.text, 'html.parser')

scoreDiv = soup.find('div',{'class': 'cb-lv-scrs-col'})
additionalMessage = soup.find('div',{'class': 'cb-text-live'})

print(scoreDiv.text)
print(additionalMessage.text)

sp.run(['notify-send','{}\r{}'.format(scoreDiv.text,additionalMessage.text)])