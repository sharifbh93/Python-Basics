from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")


class Multi_Select:
    def multiselect(self):
        driver.get("https://semantic-ui.com/modules/dropdown.html")
        dd_demo = driver.find_element(By.CSS_SELECTOR, ".ui.fluid.dropdown.selection.multiple.active.visible")
        dd_multi = Select(dd_demo)

        dd_multi.select_by_value("angular")
        time.sleep(1)
        dd_multi.select_by_index(1)
        time.sleep(1)
        dd_multi.select_by_visible_text("CSS")
        time.sleep(1)
        dd_multi.select_by_index(4)
        time.sleep(5)


demo_multi = Multi_Select
demo_multi.multiselect(Multi_Select)
