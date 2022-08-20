import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path= "C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")

driver.get("https://www.sugarcrm.com/au/request-demo/")
driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
driver.maximize_window()
button1 = driver.find_element(By.ID, 'doi0').is_selected()
print(button1)
driver.find_element(By.ID,'doi0').click()
button3 = driver.find_element(By.ID,'doi0').is_selected()
print(button3)
driver.find_element(By.ID, 'doi1').click()
button2 = driver.find_element(By.ID, 'doi1').is_selected()
print(button2)
driver.close()