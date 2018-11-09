from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = 'admin'
pwd = 'pwd'

browser = webdriver.Firefox()

browser.get("http://192.168.99.100:8080/")

username = browser.find_element_by_name("login")
username.send_keys(user)

password =browser.find_element_by_name("mdp")
password.send_keys(pwd)

password.send_keys(Keys.RETURN)
