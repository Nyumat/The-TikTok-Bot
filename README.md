<p align="center">
  <img width="460" height="300" src="https://tricolortimes.com/wp-content/uploads/2020/02/Reviews_Larsen-Whitnie_TikTok.svg">
  
 <div align="center">
 <img src="https://img.shields.io/github/languages/top/Nyumat/TheTikTokBot">
 <img src="https://img.shields.io/badge/license-MIT-green">
 <img src="https://img.shields.io/github/last-commit/Nyumat/TheTikTokBot">
 <img src="https://img.shields.io/badge/version-v2-blue">

 </div>

<h3 align="center" style="font-size: 1.5rem;"> [PATCHED.] </h3>
<h1 align="center" style="font-size: 4rem;">The TikTok Bot</h1>

<p align="center" style="font-size: 1rem;">Made By <a src="github.com/nyumat">Nyumat.</a></p>
<br>


<h2 align="center"> See <a href="https://github.com/Nyumat/The-TikTok-Bot/issues/11"> here</a>
  and <a href="https://github.com/Nyumat/The-TikTok-Bot/issues/10"> here</a> for why, and, what's next for this project.</h2>

<b><h3 align="center">Disclaimer: This bot is for educational purposes, only.</h3></b>
<br>
<br>

## Patch Explanation

* The Selenium version is patched. 
* However, FireLiker.com is still an active service on the internet, [here](fireliker.com)
* The requests version is also patched. TikTok.com's API is no longer accessible with normal, non-authed headers. (I still can't believe it was at some point.)
* You can make your own bot instance with this latest commit for another service, such as instagram for example.


## Getting Started

* There's a selenium version and a concurrent, http requests version. 
* The selenium version requires a re-write and is barring any revisions to the fireliker.com site, is non-useful (There's a CAPTCHA).
* The requests version was the original bot, and had its hayday, but is patched as well.
* I've comitted changes which will make it easier for developers to create their own bot instance for plug-in-play type use on any social media API. 
* Most if not all of the TikTok related inputs can be revised as needed for your use case.

## Proxies 

The bot scrapes proxies from [free-proxy-list.net.](https://free-proxy-list.net) Here's an example method from the TikTokBot class, with comments explaining the process. The reason this is important is because the proxies are what allow the bot to appear unique to clients.

> Note, you may or may not need to create a solution to determine if the proxy is working as free proxies tend to be the most unreliable. Although I will say I've had decent luck so far.

```python
def get_elite_proxies(use_http=True):
      # Generate a random user agent.
      ua = UserAgent()
      user_agent = ua.random
      # Our proxy solution.
      url = 'https://free-proxy-list.net/'
      # Define the headers for the request.
      ua_header = {'User-Agent': user_agent}
      content = requests.get(url, headers=ua_header).text
      # Our web scraper, bs4 gives us the HTML elements on the page.
      soup = BeautifulSoup(content, 'html.parser')
      rows = []
      # It through the table rows we need to scrape for further processing
      for row in soup.findAll("tr"):
          rows.append(row)
      elite_https_proxies = []
      # If use_http is false, we'll be using the non-https proxy ips.
      elite_proxies = []
      # Futher process each row to grab the ip
      for row in rows:
        # Get the cells 
          i = row.findAll('td')
          try:
             # Here/Below, we're just writing to files storing the ip and port.
             # This can be mofidied for your use case with the bot instance.
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
      # Depending on the argument passed in, we'll use the https list or not.
      return "\n".join([str(i) for i in elite_https_proxies]) if use_http == True else "\n".join([str(i) for i in elite_proxies])

```

## Closing Thoughts

It was a solid run and honestly, even though this project is now an artifact, I'm thankful for what were able to achieve and show to the world in 2020. 

I can forsee a new social media application being creted in the next couple years possibly allowing us to take advantage of weak API design. 

 But until then, we'll have to all move forward. Peace ✌🏿


## License

[![License](https://img.shields.io/badge/license-MIT-greene)](http://badges.mit-license.org)
- **[MIT license](LICENSE.txt)**
