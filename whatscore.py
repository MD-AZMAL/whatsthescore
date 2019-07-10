import requests
from bs4 import BeautifulSoup
import os
import subprocess as sp

match_url = 'https://www.cricbuzz.com/cricket-match/live-scores'



def getscore():
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

            print(scoreDiv)
            print(additionalMessage)
            sp.run(['notify-send','{}\r{}'.format(scoreDiv,additionalMessage)])
        prevScore = scoreDiv

if __name__ == '__main__':
    try:
        getscore()
    except KeyboardInterrupt:
        print('Bye!')
        exit(0)