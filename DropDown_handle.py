import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DropDown():
    def demodropdown(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        Jobtitle = driver.find_element(By.NAME,"UserTitle")
        dd = Select(Jobtitle)

        dd.select_by_index(1)
        time.sleep(2)

        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(2)

        dd.select_by_visible_text("IT Manager")
        time.sleep(2)

DD = DropDown
DD.demodropdown(DropDown)