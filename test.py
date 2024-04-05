from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def login(username,password):
    if username in username_list and password in password_list:
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys(username)
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('secret_sauce')
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@type='submit']").click()
        driver.find_element(By.XPATH,"//select").click()
        time.sleep(1)
        driver.find_element(By.XPATH,"//select/option[@value='hilo']").click()

        prices=driver.find_elements(By.XPATH,"//div[@class='inventory_item_description']/div/following-sibling::div/div")
        # desc=driver.find_elements(By.XPATH,"//div[@class='inventory_item_description']/div/a/div")[2].text
        list2=[]
        for i in range(len(prices)):
            list2.append(prices[i].text)
        third_highest=list2[-3]
        print(third_highest)
        for i in range(len(prices)):
            if list2[i]==third_highest:
                print(driver.find_elements(By.XPATH,"//div[@class='inventory_item_label']/a/div")[i].text)
                print(driver.find_elements(By.XPATH,"//div[@class='inventory_item_desc']")[i].text)


driver = webdriver.Chrome()
driver.implicitly_wait(7)
driver.get("https://www.saucedemo.com/")
username_text=driver.find_element(By.XPATH,"//div[@id='login_credentials']").text
username_list=username_text.split("\n")
username_list.pop(0)
password_text=driver.find_element(By.XPATH,"//div[@class='login_password']").text
password_list=password_text.split("\n")
password_list.pop(0)
login('standard_user','secret_sauce')
time.sleep(7)
driver.close()