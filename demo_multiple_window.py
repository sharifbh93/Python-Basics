from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class Multiple_window:
    def demoMW(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        parent_handle = driver.current_window_handle
        driver.find_element(By.XPATH, "//a[@title='Yatra Gift Cards']//img[@class='conta iner large-banner']").click()
        time.sleep(2)
        all_handles = driver.window_handles
        print(all_handles)
        for childhandle in all_handles:
            if childhandle != parent_handle:
                driver.switch_to.window(childhandle)
                driver.find_element(By.XPATH, "//a[normalize-space()='Shop Now']").click()
                time.sleep(3)

                driver.close()
        driver.switch_to.window(parent_handle)
        current_handles = driver.window_handles
        print(current_handles)
        time.sleep(2)
        for secondchild in current_handles:
            if secondchild != parent_handle:
                driver.switch_to.window(secondchild)
                time.sleep(2)
                driver.find_element(By.XPATH,"//input[@id='denomination']").send_keys("924")
                time.sleep(3)


demo_MW = Multiple_window
demo_MW.demoMW(Multiple_window)