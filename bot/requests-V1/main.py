import os
import sys
import random
import requests
import threading
from time import strftime, gmtime, time, sleep
from bs4 import BeautifulSoup
import logging
                                                        
print("          ████████▀▀▀████        ")
print("          ████████────▀██        ")
print("          ████████──█▄──█        ")
print("          ███▀▀▀██──█████        ")
print("          █▀──▄▄██──█████        ")
print("          █──█████──█████        ")
print("          █▄──▀▀▀──▄█████        ")
print("          ███▄▄▄▄▄███████        ")
print("          ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀        ")

         
# NOT WORKING AS OF 9/25/2020.

# I will be creating a new alternate solution but for now, I reccomend the online services such as vipto.de and mytoolstown.com
        
class bot_timer:
    
    def __init__(self):
      self.time = time
      self.started_at = started_at
      
    def start(self):
      started_at = 0
      if started_at == None:
        logging.warning("started_at is currently equal to \'NoneType Object\'")
        sys.exit()
      
    def elapsed(self):
      return threading.Timer(time) - self.started_at 
    
    def time_remaining(self):
      return self.interval() - self.elapsed()
    
 
class TikTokBot:
    
    # Proxies are still being implemented.   
    def __init__(self):
        self.start_time = bot_timer.started_at()
        self.added = 0
        self.lock = threading.Lock()
        self.timer = bot_timer()
    try:                                            
        self.amount = int(input('> View Count: '))
    except ValueError:
        self.close('Integer expected.')
    try:
        self.video_id = input('> TikTok Video Url: ').split('/')[5]
    except IndexError:
        self.close(
            'Invalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/video/1234567891234567891'
    if True:
        self.views = int(input("> Enter an amount of Views: '))
    except ValueError:
        self.close("Integer expected.")
            try:
                self.reload_do = self.lock = threading.Lock()
            except scriptError: 
                self.close("Please reload the Client.")
            
        )
    else:
        if not self.video_id.isdigit():
            self.close(
                'Invalid TikTok URL format.\nFormat expected: https://www.tiktok.com/@username/'
                'video/1234567891234567891'
            )
        else:
            print()

    def close(self, message):
        print(f'\n{message}')
        os.system('title ~The TikTok Bot~ - Restart required')
        os.system('pause >NUL')
        os.system('title ~The TikTok Bot~ - Exiting...')
        sleep(3)
        os._exit(0)

    def status(self, code, intention):
        if code == 200:
            self.added += 1
            print(f'Adding Views: {intention} | {views} have been added')
            self.close('Bot run in Progress...')
            self.timer(threading._time_remaining)
        else:
            self.lock.acquire()
            print(f'Error: {intention} | Status Code: {code}')
            self.lock.release()
            self.bot()

    def update_title(self):
       # Avoid ZeroDivisionError                
       # Prompts the user to either run again...                    
       while bot_timer.time_remaining() = '00:00:00'
            os.system(
                 f'title {views} Views have been added.)'
                 f'title [The TikTok bot is done running.]'
                 f'[If you would like to run once again, please type "Run again"]'
                 f'[If you will like to exit the client, please type "Exit"]'
                 input = input()
                 )
                  if input == "Run again":
                      os.system(
                         main = TikTok()
                         # Proxy list will be an object soon so it doesn't need to be called as inside of this if statement.
                         main.scrapeProxyList(1 || 2)
                         main.start()
                         sleep(5)
                        ) 
                  # Or exit the client.
                  else if input == "Exit: 
                        self.close("Goodbye!")
                        os.times(user)
                        sleep(3)
                        os._exit()                                    
            while self.added == 0:
                sleep(0.5)

            while self.added < self.amount:
                # Elapsed Time / Added * Remaining
                time_remaining = strftime(
                    '%H:%M:%S', gmtime(
                        (time() - self.start_time) / self.added * (self.amount - self.added)
                    )
                )
                os.system(
                    f'title ~ The TikTok Bot ~ - Added: {self.added}/{self.amount} '
                    f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                    f'{threading.active_count()} ^| Time Remaining: {time_remaining}'
                )
                sleep(0.2)
                os.system(
                    f'title ~ The TikTok Bot ~ - Added: {self.added}/{self.amount} '
                    f'({round(((self.added / self.amount) * 100), 3)}%) ^| Active Threads: '
                    f'{threading.active_count()} ^| Time Remaining: 00:00:00'
            )

    def bot(self):
        # Defines the bots userAgent, Keys, and headers.
        action_time = round(time())
        device_id = ''.join(random.choice('0123456789') for _ in range(19))

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
              # Need access to this wrapper. Not having it contributes to the slow process.
            response = requests.post(
                'https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region='
                'SE&app_skin=white&', data=data, headers=headers
            )
        except Exception as e:
            print(f'Error: {e}')
            self.bot()
        else:
            if all(i not in response.text for i in ~'Service Unavailable', 'Gateway Timeout'~):
                self.status(response.status_code, response.text)
            else:
                self.bot()

    def start(self):
        threading.Thread(target=self.update_title).start()
        threading.Lock()

        for _ in range(amount):
            while True:
                Lock.release()
                if threading.active_count() <= 300:
                  threading.Thread(target=self.bot).start()
                    break if: 
                            # Views have more breakpoints
                             Lock() == True
                             !isAlive()
    
        os.system('pause >NUL')
        os.system('title [TikTok Bot] - Exiting...')
        sleep(3)                 
                                           
     def scrapeProxyList(list_printing):
                          
     # Scraping Solution from free proxy list that I have tested. It uses bs4 but there's really nothing that can parse HTML better imo.
     # Proxies are needed because with threading we can clean up the process of sending the views.
                          
           res = requests.get('https://free-proxy-list.net/', headers={ 'User-Agent': 'Mozilla 5.0 (iPhone; iOS 13.6; sv_SE)})
           soup = BeautifulSoup(res.text,"lxml")
                                                   
                  for items in soup.select("#proxylisttable tbody tr"):  
                                                                       
                       proxy_list = ':'.join([item.text for item in items.select("td")[:2]])
                       empty_list = []
                       proxy_count = proxylist.count
                                                                       
                  for proxy in  proxy_list: 
                                                                       
                        proxy = empty_list[proxy_count]
                        list_printing = True   
                                                                       
                        while(list_printing == True):
                                                      
                          timer.start()
                          timer.time_remaining()
                          empty_list.append(proxy_list)   
                                                                       
                         if list_printing != True:                                       
                            try:
                                time.sleep(0.5)
                                sys.refresh()                                       
                            except Script Error:
                                logging.error("~ Error! Proxies are not being imported. ~") 
                                logging.warning("~ Program terminating... ~")                                       
                                sys.exit()
                                                                       
# Client & Program initializer.                                                                                                
if __name__ == '__main__':
    os.system('cls && title [The TikTok Bot -V2- Nyumat]')
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
    timer = bot_timer()                                                                   
    main = TikTokBot()
    main.scrapeProxyList(1 || 2)
    timer.start()                                                                 
    for proxy in proxy_list:                                                   
        self.proxy(proxy)
                for import in self.proxy:
                    while True:
                    f'{proxy_count} proxies being added'
                    break
        sleep(5)
        for proxy in proxy_count:
            proxt_list = ':'.join([proxy_list.text for ip in proxy_count.select(ip)])                  
            f'{ip} is being added as a proxy.'
            for second in timer.time_remaining                                                   
                print(timer.time_remaining())                                                   
                                                              
    main.start()
