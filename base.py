from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
class BasePage:
    def __init__(self,driver):
        self.driver=driver

    def sleep_for_seconds(self,seconds=1):
        time.sleep(seconds)

    def launch(self,url):
        self.driver.get(url)
        self.driver.maximize_window()

    def getLocator(self,locatorType):
        locatorType=locatorType.lower()
        if locatorType=="id":
            return By.ID
        elif locatorType=="xpath":
            return By.XPATH
        else:
            print("wrong locator")
    def find_element(self,locatorType,value):
        locatorType=locatorType.lower()
        findByType=self.getLocator(locatorType)
        element=self.driver.find_element(findByType,value)
        return element
    def find_elements(self,locatorType,value):
        locatorType=locatorType.lower()
        findByTypes=self.getLocator(locatorType)
        elements=self.driver.find_elements(findByTypes,value)
        return elements



