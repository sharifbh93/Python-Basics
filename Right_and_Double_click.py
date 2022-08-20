from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Right_click:
    def demo_right_click(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        achains = ActionChains(driver)
        # rightClk = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        # achains.context_click(rightClk).perform()
        # time.sleep(2)
        # copyelem = driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        # copyelem.click()
        # time.sleep(5)

#         Double click

        doubleclk = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
        achains.double_click(doubleclk).perform()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(4)
rightclick = Right_click
rightclick.demo_right_click(Right_click)