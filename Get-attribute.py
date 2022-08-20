from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\browserdrivers\\chromedriver.exe")

class getAttribiuteValue:

    def attributevalue(self):

        driver.get("https://www.yatra.com/")
        attr_value = driver.find_element(By.XPATH, "//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/input[1]").get_attribute("value")
        print(attr_value)

attrobj = getAttribiuteValue
attrobj.attributevalue(getAttribiuteValue)

