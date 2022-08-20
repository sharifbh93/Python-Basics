from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")

class hidden_element:
    def shownhiddenelmt(self):
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        elem = driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[3]").is_displayed()
        print(elem)
        driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/button[1]").click()
        elem1 = driver.find_element(By.XPATH, "//body[1]/div[7]/div[1]/div[1]/div[3]").is_displayed()
        print(elem1)


Displayed = hidden_element
Displayed.shownhiddenelmt(hidden_element)
