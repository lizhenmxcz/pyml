# @Time 2016/11/3 14:46
# @Author lizhenmxcz@163.com
# @Todo use selenium to auto test the website

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys
import os,time
import random


class WebTest:

    driver = webdriver.Chrome()
    f = open("dict.txt", "r")
    lines = f.readlines()

    @staticmethod
    def randomText(num):
        return random.sample('abcdefghijklmnopqrstuvwxyz', num)

    @staticmethod
    def randomNum(num):
        return random.sample('0123456789', num)

    def testPeruggia(self, loopNum):
        self.driver.get("http://192.168.55.35/peruggia/index.php?action=login")
        for line in self.lines:
            try:
                self.driver.find_element_by_name("username").send_keys(line.split()[0])
                self.driver.find_element_by_name("password").send_keys(line.split()[1])
                self.driver.find_element_by_name("password").send_keys(Keys.ENTER)
            except NoSuchElementException:

                time.sleep(3)
                length = len(self.driver.find_elements_by_link_text("Comment on this picture"))
                for j in range(loopNum):
                    for i in range(length):
                        links = self.driver.find_elements_by_link_text("Comment on this picture")
                        link = links[i]
                        link.click()
                        self.driver.find_element_by_name("comment").send_keys(self.randomText(20))
                        self.driver.find_element_by_tag_name("input").click()

    def testGetboo(self):

        for line in self.lines:
            try:
                self.driver.get("http://192.168.55.35/getboo/login.php")
                self.driver.find_element_by_name("name").send_keys(line.split()[0])
                self.driver.find_element_by_name("pass").send_keys(line.split()[1])
               # time.sleep(3)
                self.driver.find_element_by_name("submitted").click()
               # time.sleep(3)
                self.driver.find_element_by_link_text("Forgot password?").click()
               # time.sleep(3)
                self.driver.find_element_by_name("aname").send_keys(self.randomText(8))
                self.driver.find_element_by_name("email").send_keys(self.randomText(8), "@",
                                                                    self.randomText(6), ".", self.randomText(3))
                self.driver.find_element_by_name("submitted").click()
            except WebDriverException:
                time.sleep(13)

    def testCookie(self):
        self.driver.get("http://owaspbwa/getboo/login.php")
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print(cookie)

    def testWordPressComment(self):
        self.driver.get("http://owaspbwa/wordpress/wp-login.php")
        # for line in self.lines:
        #     try:
        #         self.driver.find_element_by_name("log").clear()
        #         self.driver.find_element_by_name("pwd").clear()
        #         self.driver.find_element_by_name("log").send_keys(line.split()[0])
        #         self.driver.find_element_by_name("pwd").send_keys(line.split()[1])
        #         # time.sleep(3)
        #         self.driver.find_element_by_name("submit").click()
        #     except NoSuchElementException:
        #         time.sleep(10)
        #         for i in range(15):
        #             self.driver.get("http://owaspbwa/wordpress/?p=", i+1)
        #             self.driver.find_element_by_name("comment").send_keys(self.randomText(30))
        #             self.driver.find_element_by_name("submit").click()
        self.driver.find_element_by_name("log").send_keys("user")
        self.driver.find_element_by_name("pwd").send_keys("aaaaa")
        #         #
        self.driver.find_element_by_name("submit").click()

        for i in range(38):
            try:
                url = "http://owaspbwa/wordpress/?p="+str(i)
                self.driver.get(url)
                time.sleep(3)
                self.driver.find_element_by_name("comment").send_keys(self.randomText(20))
                self.driver.find_element_by_name("submit").click()
                time.sleep(12)
            except NoSuchElementException:
                continue

    def testWordPressPost(self):
        self.driver.get("http://owaspbwa/wordpress/wp-login.php")
        self.driver.find_element_by_name("log").send_keys("admin")
        self.driver.find_element_by_name("pwd").send_keys("aaaaa")
        self.driver.find_element_by_name("submit").click()

        time.sleep(2)
        self.driver.find_element_by_link_text("Write a post").click()
        for i in range(10):
            self.driver.find_element_by_name("post_title").send_keys(self.randomText(10))
            self.driver.find_element_by_name("content").send_keys(self.randomText(20))
            self.driver.find_element_by_name("publish").click()
            time.sleep(3)

    def testGuessnum(self):
        self.driver.get("http://owaspbwa/vicnum/guessnum.html")
        self.driver.find_element_by_name("player").send_keys(self.randomText(6))
        self.driver.find_element_by_name("player").send_keys(Keys.ENTER)
        i = 0
        while True:
            if i > 200:
                break
            try:
                self.driver.find_element_by_name("userguess").send_keys(self.randomNum(3))
                self.driver.find_element_by_name("userguess").send_keys(Keys.ENTER)
                i += 1
            except NoSuchElementException:
                break

    def __del__(self):
        self.driver.close()
        self.f.close()

if __name__ == '__main__':

    test = WebTest()
    test.testPeruggia(3)
    test.testGetboo()
    test.testWordPressPost()
    test.testWordPressComment()
    test.testGuessnum()
