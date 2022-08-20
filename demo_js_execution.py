from selenium import webdriver
import time

class JavaScript:
    def Demojs(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        # driver.get("https://www.rcvacademy.com/home-2/")
        driver.execute_script("window.open('https://training.rcvacademy.com/', '_self')")
        time.sleep(3)
        demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[0].click();", demo_element)

JS = JavaScript
JS.Demojs(JavaScript)