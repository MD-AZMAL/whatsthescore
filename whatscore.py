import requests
from bs4 import BeautifulSoup
import os
import subprocess as sp
import time 

match_url = 'https://www.cricbuzz.com/cricket-match/live-scores'

def notify_me(scoreDiv,additionalMessage):
    print(scoreDiv)
    print(additionalMessage)
    sp.run(['notify-send','{}\r{}'.format(scoreDiv,additionalMessage)])

def getscore():
    startTime = time.time()
    prevScore = ''
    while True:
        res = requests.get(match_url)
        soup = BeautifulSoup(res.text, 'html.parser')

        scoreDiv = soup.find('div',{'class': 'cb-lv-scrs-col'}).text 
        
        try:
            additionalMessage =  soup.find('div',{'class': 'cb-text-complete'}).text
        except:
            try:
                additionalMessage = soup.find('div',{'class': 'cb-text-live'}).text
            except:
                additionalMessage = ''

        if scoreDiv != prevScore:
            notify_me(scoreDiv,additionalMessage)
        elif abs(int(time.time() - startTime)) >= 120:
            print(time.time() - startTime)
            startTime = time.time()
            notify_me(scoreDiv,additionalMessage)

        prevScore = scoreDiv

if __name__ == '__main__':
    try:
        getscore()
    except KeyboardInterrupt:
        print('Bye!')
        exit(0)