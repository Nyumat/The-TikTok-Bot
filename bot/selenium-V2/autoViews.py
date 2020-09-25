from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Currently, The Selenium Version that exploited FireLiker.com is patched.
# A fix will be in production within the next week or so.

# Links that through getURL will be referenced
mainURL = "https://fireliker.com/"
panelURL = "https://fireliker.com/welcome.php"
autoviewURL = "https://fireliker.com/autoviews.php"
loop = False

# Prompt the user for their information and desired views.
print("What is your TikTok user name?")
user = input("-->>  ")

print("How many views would you like?")
print("Options are : [1000] [800] [600] [400] [200] ")
views = input("")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()
driver.set_window_size(500, 540)
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
# Select Specified  Views logic
if views == "1000":
    select.select_by_value('5')
elif views == "800":
    select.select_by_value('4')
elif views == "600":
    select.select_by_value('3')
elif views == "400":
    select.select_by_value('2')
elif views == "200":
    select.select_by_value('1')
else:
    # User didn't enter one of the dropdown values
    print("You  did not specify a number of views within  range, please re-run the program.")
    breakpoint()
select_button = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/button").click()

# Code below isn't needed unless you're in a headless browser.

#select = driver.find_element_by_id("select").click()
#select_views = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/div/select/option[5]").click()
#time.sleep(3)
#send_views = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[2]/div/form/button")
#time.sleep(2)

# Wait 5 mins to run again.
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
