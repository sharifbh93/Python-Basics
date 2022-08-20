from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class ScreenShot:
    def ScreenS(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        continuedemo = driver.find_element(By.XPATH, "//*[@id='login-continue-btn']")
        continuedemo.screenshot(".\\test0.png")
        continuedemo.click()
        time.sleep(2)
        continuedemo.screenshot("E:\\error.png")
        time.sleep(2)
        driver.save_screenshot("E:\\error2.png")


demosreenshot = ScreenShot
demosreenshot.ScreenS(ScreenShot)
