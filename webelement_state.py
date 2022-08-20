from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")

class web_elmt_state():
    def webelmtstate(self):
        driver.get("https://training.openspan.com/login")
        driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/form[1]/table[1]/tbody[1]/tr[1]/td[1]/input[1]").send_keys("kafjdl")
        driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/div[2]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/input[1]").send_keys("kaafk")
        time.sleep(2)
        state = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/form/table/tbody/tr[3]/td/input").is_enabled()

        print(state)

status = web_elmt_state
status.webelmtstate(web_elmt_state)