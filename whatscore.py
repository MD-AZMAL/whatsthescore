import requests
from bs4 import BeautifulSoup
import os
import subprocess as sp
import time

match_url = 'https://www.cricbuzz.com/cricket-match/live-scores'


def notify_me(match, scoreDiv, additionalMessage):
    print(match)
    print(scoreDiv)
    print(additionalMessage)

    sp.run(['notify-send', '{}\r{}\r{}'.format(match, scoreDiv, additionalMessage)])


def getscore():

    startTime = time.time()
    prevScore = ''

    while True:
        res = requests.get(match_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        scoreDiv = soup.find_all('div', {'class': 'cb-lv-scrs-col'})[0].text
        match = soup.find_all(
            'a', {'class': 'text-hvr-underline'})[0].text[:-1]

        if scoreDiv[-1] != '}':
            scoreDiv = scoreDiv + 'yet to bat'

        try:
            additionalMessage = soup.find_all(
                'div', {'class': 'cb-text-live'})[0].text
        except:
            try:
                additionalMessage = soup.find_all(
                    'div', {'class': 'cb-text-complete'})[0].text
            except:
                additionalMessage = ''

        if scoreDiv != prevScore:
            notify_me(match, scoreDiv, additionalMessage)
        elif abs(int(time.time() - startTime)) >= 120:
            print(time.time() - startTime)
            startTime = time.time()
            notify_me(match, scoreDiv, additionalMessage)

        prevScore = scoreDiv

        time.sleep(5)


if __name__ == '__main__':
    try:
        getscore()
    except KeyboardInterrupt:
        print('Bye!')
        exit(0)
