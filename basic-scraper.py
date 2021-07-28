#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time


# Initialize ChromeDriver
options = Options()
options.headless = False
options.add_argument("no-sandbox")
options.add_argument("--window-size=683,768")
options.add_argument("--window-position=683,0")
driver = webdriver.Chrome(options=options)

# initial request 
driver.get('https://quotes.toscrape.com/')
waitTime = WebDriverWait(driver, 20)

all_links=driver.find_elements_by_xpath("//div[@class='quote']/span[1]")

# check result for expected search criteria
for link in all_links:
    if 'beauty' in link.text:
        print(link.text)

driver.quit()

