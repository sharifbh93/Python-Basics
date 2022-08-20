from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class iFrame:
    def iframe_demo(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")

        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH,"(//div[@class='w3-bar w3-card-2 notranslate'])[1]"))
        time.sleep(2)
        driver.find_element(By.XPATH,"//iframe[@title='W3Schools Free Online Web Tutorials']").click()
        time.sleep(3)
        print(driver.find_element(By.XPATH,"//a[@id='w3loginbtn']").is_selected())
        time.sleep(2)

demoiframe = iFrame
demoiframe.iframe_demo(iFrame)