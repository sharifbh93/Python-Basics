from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class Demo_PopUp:
    def Handle_PopUp(self):
        driver = webdriver.Chrome(executable_path="C:\\browserdrivers\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        time.sleep(2)
        # Accept alert
        button = driver.find_element(By.XPATH,"/html[1]/body[1]/button[1]")
        button.click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.accept()
        time.sleep(2)

        button.click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        button.click()
        driver.switch_to.alert.send_keys("This is a pop up alert")
        time.sleep(2)
        driver.switch_to.alert.accept()
        time.sleep(2)
demoPopUp = Demo_PopUp
demoPopUp.Handle_PopUp(Demo_PopUp)