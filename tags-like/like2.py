from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instabot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/')

        time.sleep(15)
        email = bot.find_element_by_name('IG_Uname').send_keys('test')
        password = bot.find_element_by_name('PASS_HERE')
        
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(keys.Return)
        time.sleep(30)

    def like(self, hashtag):
        count = 0
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'')
        time.sleep(3)


object = Instabot('IG_Uname', 'PASS_HERE')
object.login()
object.like('pythonprogramming')
        
