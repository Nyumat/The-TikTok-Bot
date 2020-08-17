import  math
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pygame

from time import sleep

#Ask how many views you want
viewsSelected = input("How many views would you like to add? : ")
video_url = input("What is the url for the video that you would like to add the views to?")


# Set the web browser to chrome.
options = webdriver.ChromeOptions()
options.add_argument("/private/var/folders/mz/5gznz0hn5bn071_d_tktpm5w0000gn/T/.com.google.Chrome.KaYEXP/Default") #Path to chrome profile inside of [chrome://version]
chrome_path ='/Users/tnyuma/Desktop/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

# Iteratively opens a new tab.
def openTab(tabs):
    num_tabs = tabs
    open_tab = tabs.send_keys(Keys.COMMAND, "T")
    close = tabs.send_keys(Keys.COMMAND, "W")
    open_it = open_tab

for i in range(i, num_Tabs):
    open_tab
  
#Clicks the URL Link Bar
search_bar = driver.find_element_by_name("searchinput").click()
time.sleep(1)

#Type in the given URL into the bar
actions = ActionChains(driver)
actions.send_keys(video_url)
actions.perform()
time.sleep(1)
actions.perform()

#Click search Video
search_video_button = driver.find_element_by_xpath("/html/body/b/div[2]/form/div/center/input").click()
time.sleep(1)

#After your specified video pops up, click the submit button.

def deleteCookiesAc():
    deleteCookies = driver.delete_all_cookies
    print("Cookies Deleted.")
    deleteCookies()

driver.refresh()
time.sleep(2)

deleteCookiesAc()
time.sleep(2)


time.sleep(2)

# Creates new guest requests
