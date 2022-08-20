from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By


class AutoSugg:
    def auto_sugg(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()

        driver.get("https://www.yatra.com")
        # driver.switch_to.alert.accept()
        depart_from = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        driver.implicitly_wait(10)
        # depart_from.click()

        depart_from.send_keys("New Delhi")

        depart_from.send_keys(Keys.ENTER)

        print(depart_from.is_selected())

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New York")

        going_to.send_keys(Keys.ENTER)


        driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()


        # for search in search_result:
        #
        #     if "New York (JFK)" in search_result.text:
        #         search_result.send_keys(Keys.ENTER)
        #         time.sleep(3)
        #         break

        all_dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "25/07/2022":
                date.click()
                time.sleep(5)
                break


autosugg = AutoSugg
autosugg.auto_sugg(AutoSugg)
