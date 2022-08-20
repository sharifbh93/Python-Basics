from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")

class DriverMethod:

    def demo_browser(self):

        driver.get("https://www.yatra.com/")
        print(driver.title)
        print(driver.current_url)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Yatra for Business').click()
        driver.back()
        text = driver.find_element(By.LINK_TEXT, "Yatra for Business")
        print(text)
        time.sleep(2)
        driver.close()


driverfunction = DriverMethod
driverfunction.demo_browser(DriverMethod)



