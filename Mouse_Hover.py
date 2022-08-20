from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Mouse_Hover:
    def demo_mouse_hover(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        homepage = ("https://www.yatra.com/")
        driver.get(homepage)
        print(driver.current_window_handle)
        # time.sleep(2)
        # print(driver.switch_to.alert.text)
        time.sleep(2)
        more_button = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        my_account_link = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle']")

        achains = ActionChains(driver)
        achains.move_to_element(more_button).perform()
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(10)
        # driver.back()
        # time.sleep(5)
        # print(driver.current_window_handle)
        # achains.move_to_element(my_account_link).perform()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "//a[@title='My Bookings']").click()
        # time.sleep(3)
        # # # driver.switch_to.alert.accept()
        # # # time.sleep(2)


mouse_hover = Mouse_Hover
mouse_hover.demo_mouse_hover(Mouse_Hover)
