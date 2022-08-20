import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.sugarcrm.com/au/request-demo/")
driver.find_element(By.ID,'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,'interest_market_c0').click()
isenabled = driver.find_element(By.ID,'interest_market_c0').is_selected()
print(isenabled)
isenabled2 = driver.find_element(By.ID, 'interest_sell_c0').is_selected()
print(isenabled2)
