import os
import sys
from random import randint, choice, random
import requests
from threading import active_count, Thread
import threading
from time import strftime, gmtime, time, sleep
from bs4 import BeautifulSoup
import logging
import ssl
from pystyle import Colorate, Colors, Write
from http import cookiejar
import regex as re
from fake_useragent import UserAgent
os.system('clear')
print("          ████████▀▀▀████        ")
print("          ████████────▀██        ")
print("          ████████──█▄──█        ")
print("          ███▀▀▀██──█████        ")
print("          █▀──▄▄██──█████        ")
print("          █──█████──█████        ")
print("          █▄──▀▀▀──▄█████        ")
print("          ███▄▄▄▄▄███████        ")
print("          ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀        ")
print("\n")
print(
    '''
    =======================================
    |  Hello & Welcome to The-TikTok-Bot! |
    |This bot was once a monumetal exploit|
    |of TikTok's API. Now, it is a bot not|
    |containing any exploits, and is just |
    |purely archive. Feel use this bot to |
    |   bootstrap your own bot instance.  |
    =======================================
'''
)


class TikTokBot:

    # Proxies are still being implemented.
    def __init__(self, proxies=None):
        self.added = 0
        self.amount = 0
        self.views = 0
        self.proxy = proxies
        self.time = 0
        self.video_id = ""

    def start(self):
        self.clear()
        self.menu()

    def menu(self):
        proceed = True
        try:
            self.amount = int(input('> View Count: '))
        except ValueError:
            proceed = False
            self.close('Integer expected.')
        try:
            self.video_id = input('> TikTok Video Url: ').split('/')[5]
        except IndexError:
            proceed = False
            self.close(
                'Invalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/video/1234567891234567891'
            )
        if proceed:
            self.bot_init()

    def close(self, message):
        print(message)
        sys.exit()

    def notice(self, message):
        print(message)

    def status(self, code, intention):
        if (code == 200 and intention == "Bot Running"):
            self.added += 1
            self.notice(
                f'Views Added: {self.added}/{self.amount} ({round(((self.added / self.amount) * 100), 3)}%)')
            self.notice('Bot run in Progress...')
        else:
            if intention == "complete":
                self.notice('Bot run complete.')
                self.notice(f'Views Added: {self.added}/{self.amount}')
                self.notice(
                    f'Time Elapsed: {strftime("%H:%M:%S", gmtime(time() - self.start_time))}')
                self.notice(f'Active Threads: {threading.active_count() ^ 1}')
                self.notice(
                    f'Average Views Per Second: {round(self.added / (time() - self.start_time), 3)}')

    def update_title(self, views):
        while self.amount != self.added:
            self.added += 1
            print(f'Views Added: {self.added}')
            print('Bot run in Progress...')

        while self.added < self.amount:

            time_remaining = strftime(
                '%H:%M:%S', gmtime(
                    (time() - self.start_time) /
                    self.added * (self.amount - self.added)
                )
            )
            os.system(
                f'title ~ The TikTok Bot ~ - Added: {self.added}/{self.amount} '
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count()} ^| Time Remaining: {time_remaining}'
            )

            os.system(
                f'title ~ The TikTok Bot ~ - Added: {self.added}/{self.amount} '
                f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                f'{threading.active_count()} ^| Time Remaining: 00:00:00'
            )

    def bot_init(self):
        # Defines the bots userAgent, keys, and headers.
        action_time = round(time())
        device_id = randint(100000000000000, 999999999999999)

        data = (
            f'action_time={action_time}&item_id={self.video_id}&item_type=1&play_delta=1&stats_cha'
            'nnel=copy'
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-common-params-v2': 'version_code=16.6.5&app_name=musical_ly&channel=App%20Store&devi'
                                  f'ce_id={device_id}&aid=1233&os_version=13.5.1&device_platform=ip'
                                  'hone&device_type=iPhone10,5',
            'User-Agent': 'TikTok 16.6.5 rv:166515 (iPhone; iOS 13.6; sv_SE) Cronet'
        }

        try:
            """
            We no longer have acess to the old api solution, but I did some reverse search through my router and found this.

            These are the api domains in which my tiktok app has been networking within my network. 

            [There is  possibility none of these work anymore since it's been a few years, but I'm sure you can find some yourself.]

            api16-core-c-alisg.tiktokv.com
            api16-core-c-useast1a.tiktokv.com
            api16-core-va.tiktokv.com
            api19-core-c-useast1a.tiktokv.com
            api19-core-va.tiktokv.com
            api19-normal-c-useast1a.tiktokv.com
            api21-core-c-alisg.tiktokv.com
            api22-core-c-useast1a.tiktokv.com
            api22-normal-c-useast1a.tiktokv.com

            """
            response = requests.post(
                'See_Doc', data=data, headers=headers,
                proxies=self.proxy, timeout=10
            )

            self.start(self.amount, self.proxy)

        except Exception as e:
            print(f'Error: {e}')
            self.bot()

    def start(self):
        self.start_time = time()

        self.amount = input('> View Count: ')
        self.video_id = input('> TikTok Video Url: ')

        self.amount = int(self.amount)
        self.added = 0

        while self.added < self.amount:
            # Creates a new thread for each proxy.
            threading.Thread(target=self.status(
                200, "Bot Running", ), daemon=True, args=(self.proxy,)).start()

            if self.added >= self.amount:
                self.status(200, "complete")

    def get_elite_proxies(use_http):
        ua = UserAgent()
        user_agent = ua.random
        url = 'https://free-proxy-list.net/'
        ua_header = {'User-Agent': user_agent}
        content = requests.get(url, headers=ua_header).text
        soup = BeautifulSoup(content, 'html.parser')
        rows = []
        for row in soup.findAll("tr"):
            rows.append(row)
        elite_https_proxies = []
        elite_proxies = []
        for row in rows:
            i = row.findAll('td')
            try:
                if use_http == True:
                    if (i[4].text == 'elite proxy') and i[6].text == 'yes':
                        with open('elite_proxies.txt', 'r+') as f:
                            last_line = f.readlines()[-1]
                            f.write(i[0].text + ':' + i[1].text)
                            f.write('\n')
                        elite_https_proxies.append(i[0].text + ':' + i[1].text)
                else:
                    if (i[4].text == 'elite proxy') and i[6].text == 'no':
                        with open('elite_proxies.txt', 'r+') as f:
                            last_line = f.readlines()[-1]
                            f.write(i[0].text + ':' + i[1].text)
                            f.write('\n')
                        elite_proxies.append(i[0].text + ':' + i[1].text)
            except:
                continue
        return "\n".join([str(i) for i in elite_https_proxies]) if use_http == True else "\n".join([str(i) for i in elite_proxies])


def get_normal_proxies():
    res = requests.get('https://free-proxy-list.net/',
                       headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(res.text, "lxml")
    proxies = soup.find('textarea').text

    regex = re.compile(r'\d+\.\d+\.\d+\.\d+\:\d+')
    proxies = regex.findall(proxies)

    proxies = "\n".join([str(i) for i in proxies])
    return proxies


# Entry point
if __name__ == '__main__':
    # os.system('title' + '[The TikTok Bot -V2- Nyumat]')
    sys.stdout.write("\x1b]2;[The TikTok Bot -V2- Nyumat]\x07")
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    proxies = get_normal_proxies()
    sleep(10)
    print("Loading Proxies...")
    print(proxies + '\n')
    os.system("clear")
    print("Proxies Loaded!")
    main = TikTokBot()
    main.start()
    
    
