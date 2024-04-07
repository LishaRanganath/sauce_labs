from selenium.webdriver import Keys

from base import BasePage
from selenium import webdriver

class Main(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.url="https://www.saucedemo.com/"
    def login_details(self,username,password):
        username_text = self.find_element("xpath", "//div[@id='login_credentials']").text
        list_username=username_text.split("\n")
        list_username.pop(0)
        password_text = self.find_element("xpath", "//div[@class='login_password']").text
        password_list = password_text.split("\n")
        password_list.pop(0)
        print(list_username)
        print(password_list)
        for i in list_username:
            for j in password_list:
                user_field=self.find_element("xpath", "//input[@placeholder='Username']")
                pass_field=self.find_element("xpath", "//input[@placeholder='Password']")
                user_field.send_keys(i)
                pass_field.send_keys(j)
                self.find_element("xpath", "//input[@type='submit']").click()
                if driver.current_url=="https://www.saucedemo.com/inventory.html":
                    self.find_element("xpath","//button[@id='react-burger-menu-btn']").click()
                    self.sleep_for_seconds()
                    self.find_element("xpath","//div[@class='bm-menu']/child::nav/child::a[text()='Logout']").click()
                else:
                    user_field.send_keys(Keys.CONTROL + "a")
                    user_field.send_keys(Keys.BACKSPACE)
                    self.sleep_for_seconds()
                    pass_field.send_keys(Keys.CONTROL + "a")
                    pass_field.send_keys(Keys.BACKSPACE)
        if username in list_username and password in password_list:
            self.find_element("xpath", "//input[@placeholder='Username']").send_keys(username)
            self.find_element("xpath", "//input[@placeholder='Password']").send_keys(password)
            self.find_element("xpath", "//input[@type='submit']").click()


    def getThirdHighest(self):
        self.find_element("xpath", "//select").click()
        self.find_element("xpath", "//select/option[@value='hilo']").click()
        prices=self.find_elements("xpath","//div[@class='inventory_item_description']/div/following-sibling::div/div")
        list2 = []
        for i in range(len(prices)):
            list2.append(prices[i].text)
        third_highest = list2[-3]
        print(third_highest)
        return list2,third_highest

    def get_details(self,price_list,price):
        for i in range(len(price_list)):
            if price_list[i] == price:
                print(self.find_elements("xpath", "//div[@class='inventory_item_label']/a/div")[i].text)
                print(self.find_elements("xpath", "//div[@class='inventory_item_desc']")[i].text)


if __name__=="__main__":
    driver=webdriver.Chrome()
    main_page=Main(driver)
    main_page.launch(main_page.url)

    main_page.login_details("standard_user","secret_sauce")
    list2,third_highest=main_page.getThirdHighest()
    main_page.get_details(list2,third_highest)
