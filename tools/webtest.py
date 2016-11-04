# @Time 2016/11/3 14:46
# @Author lizhenmxcz@163.com
# @Todo use selenium to auto test the website

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os,time
import random


class WebTest:

    driver = webdriver.Chrome()

    @staticmethod
    def randomText(num):
        return random.sample('abcdefghijklmnopqrstuvwxyz&#%^*f', num)

    def testPeruggia(self):
        self.driver.get("http://192.168.55.35/peruggia/index.php?action=login")
        self.driver.find_element_by_name("username").send_keys("user")
        self.driver.find_element_by_name("password").send_keys("user")
        self.driver.find_element_by_name("password").send_keys(Keys.ENTER)

        time.sleep(3)
        length = len(self.driver.find_elements_by_link_text("Comment on this picture"))
        for i in range(length):
            links = self.driver.find_elements_by_link_text("Comment on this picture")
            link = links[i]
            link.click()
            self.driver.find_element_by_name("comment").send_keys(self.randomText(20))
            self.driver.find_element_by_tag_name("input").click()

    def testGetboo(self):
        self.driver.get("http://192.168.55.35/getboo/login.php")
        self.driver.find_element_by_name("name").send_keys(self.randomText(6))
        self.driver.find_element_by_name("pass").send_keys(self.randomText(6))
        time.sleep(3)
        self.driver.find_element_by_name("submitted").click()
        time.sleep(3)
        self.driver.find_element_by_link_text("Forgot password?").click()
        time.sleep(3)
        self.driver.find_element_by_name("aname").send_keys(self.randomText(8))
        self.driver.find_element_by_name("email").send_keys("jshf@234.com")
        self.driver.find_element_by_name("submitted").click()

    def __del__(self):
        self.driver.close()

if __name__ == '__main__':

    test = WebTest()
    test.testGetboo()
