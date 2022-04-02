# Instagram login
from selenium import webdriver
from time import sleep

#Put your own username and password below
username = 'demousername'
password = 'learnpython@123'



class Insta():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://instagram.com/')
        self.driver.maximize_window()

        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        login_button.click()
        login_button.send_keys(username)
        #sleep(5)

        password_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_button.click()
        password_button.send_keys(password)
        #sleep(5)

        login2_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login2_button.click()
        #sleep(5)


insta = Insta()
insta.login()
