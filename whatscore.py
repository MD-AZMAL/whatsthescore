import requests
from bs4 import BeautifulSoup
import os
import subprocess as sp

match_url = 'https://www.cricbuzz.com/cricket-match/live-scores'

prevScore = ''
while True:
    res = requests.get(match_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    scoreDiv = soup.find('div',{'class': 'cb-lv-scrs-col'}).text
    additionalMessage = soup.find('div',{'class': 'cb-text-live'}).text

    if scoreDiv != prevScore:

        print(scoreDiv)
        print(additionalMessage)
        sp.run(['notify-send','{}\r{}'.format(scoreDiv,additionalMessage)])
    prevScore = scoreDiv
