from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class ImplicitWait_demo:
    def Waits(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.XPATH,"//input[@id='username']").send_keys("gdhg")
        # driver.find_element(By.XPATH,"jalsfj").send_keys("kajfd")

impwait = ImplicitWait_demo
impwait.Waits(ImplicitWait_demo)