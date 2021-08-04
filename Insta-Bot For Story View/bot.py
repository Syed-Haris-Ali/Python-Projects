#pip install selenium
from selenium import webdriver
from selenium.wedriver.common.keys import Keys 
from time import sleep


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()

    def Login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        sleep(3)
        bot.find_element_by_class_name(
            "Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQJ.JkUp7.DhRcB").click()
        sleep(4)
        bot.find_element_by_xpath(('//button[contains(text(),"Not Now")]'))\
            .click()
        sleep(4)
        bot.find_element_by_xpath(('//button[contains(text(),"Not Now")]'))\
            .click()
        sleep(5)

    def openStories(self):
        bot = self.bot
        bot.find_element_by_class_name('OE3Ok').click()


go = InstaBot('username', 'password')
go.Login()
go.openStories()
