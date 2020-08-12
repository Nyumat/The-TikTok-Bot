from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

mainURL = "https://fireliker.com/"
panelURL = "https://fireliker.com/welcome.php"
autoviewURL = "https://fireliker.com/autoviews.php"
loop = True

print("What is your TikTok user name?")
user = input("-->>  ")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
driver.set_window_size(960, 540)
driver.get(mainURL)
time.sleep(2)
loginInput = driver.find_element_by_name("username")
loginInput.send_keys(user)

submit = driver.find_element_by_xpath("//[@id="alternative"]/form/fieldset/div[2]/button").click()

driver.get(panelURL)
time.sleep(2)
auto = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/fieldset/div/div/a[2]").click()

driver.get(autoviewURL)
select = Select(driver.find_element_by_xpath("//[@id="select"]"))
select.select_by_visible_text("1000 VIEWS")
view = driver.find_element_by_xpath("//[@id="home"]/div/div/div[2]/div/form/button").click()
time.sleep(5)

while loop == True:
    auto = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/fieldset/div/div/a[2]").click()

    driver.get(autoviewURL)
    select = Select(driver.find_element_by_xpath("//[@id="select"]"))
    select.select_by_visible_text("1000 VIEWS")
    time.sleep(315)
    view = driver.find_element_by_xpath("//*[@id="home"]/div/div/div[2]/div/form/button").click()
    time.sleep(5)
