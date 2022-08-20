import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdrivermanager import ChromeDriverManager

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")


class FindElements:
    def locate_by_link_text(self):
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "dropdown-toggle").click()
        lista = driver.find_element(By.TAG_NAME ,"a")
        print(lista)
        driver.close()


khafsd = FindElements()
khafsd.locate_by_link_text()


