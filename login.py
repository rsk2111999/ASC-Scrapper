import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_id=raw_input('Enter your LDAP ID ')
password=getpass.getpass('Enter your LDAP Password ')

#Starts Firefox on your machine
driver = webdriver.Firefox()

#To move the browser to a non-viewable area so that the user isn't disturbed
driver.set_window_size(100,100)
driver.set_window_position( 2000,2000)
driver.get("https://portal.iitb.ac.in/asc/Login")

elem_username = driver.find_element_by_id('login_user')
elem_password=driver.find_element_by_id('login_password')

elem_username.send_keys(user_id)
elem_password.send_keys(password,Keys.RETURN)

tables_list = driver.find_elements_by_tag_name('table')
cells=tables_list[5].find_elements_by_tag_name('td')

length=len(cells)-6
for i in range(0,length+1,6):
    print cells[i].text + ' ' + cells[i+2].text + ' ' + cells[i+4].text


logout_elem=driver.find_element_by_link_text('Logout')
logout_elem.click()
driver.close()
