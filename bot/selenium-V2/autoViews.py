from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

mainURL = "https://fireliker.com/"
panelURL = "https://fireliker.com/welcome.php"
autoviewURL = "https://fireliker.com/autoviews.php"
loop = False

print("What is your TikTok user name?")
user = input("-->>  ")

print("How many views would you like?")
views = input("")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()
driver.set_window_size(960, 540)
driver.get(mainURL)
time.sleep(2)
loginInput = driver.find_element_by_name("username")
loginInput.send_keys(user)

submit_xpath = "#alternative > form > fieldset > div:nth-child(2) > button"
submit = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/form/fieldset/div[2]/button").click()

driver.get(panelURL)
time.sleep(2)
auto = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/fieldset/div/div/a[2]").click()

driver.get(autoviewURL)
select = Select(driver.find_element_by_id('select')) 
select.select_by_value('5')
select_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/button").click()

# Code below isn't needed unless you're in a headless browser.

#select = driver.find_element_by_id("select").click()
#select_views = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/div/select/option[5]").click()
#time.sleep(3)
#send_views = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/button")
#time.sleep(2)

time.sleep(315)
loop = True

while loop == True:
    driver.get(autoviewURL)
    auto = driver.find_element_by_id("select")
    driver.get(autoviewURL)
    select = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/button").click()
    select.select_by_visible_text("1000 VIEWS")
    time.sleep(315)
    view = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/button")
    time.sleep(5)
