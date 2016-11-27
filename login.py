from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_id=raw_input('Enter your LDAP ')
password=raw_input('Enter your LDAP Password ')

#Starts Firefox on your machine
driver = webdriver.Firefox()
driver.get("https://portal.iitb.ac.in/asc/Login")

elem_username = driver.find_element_by_id('login_user')
elem_password=driver.find_element_by_id('login_password')

elem_username.send_keys(user_id)
elem_password.send_keys(password,Keys.RETURN)
