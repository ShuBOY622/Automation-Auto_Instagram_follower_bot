
#Remember to edit Your username, password and the exact account name you want


import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
UserId="Your_UserID"
Passwd="PASSWORD"
Account="Shah Rukh Khan"  #for example

driver_path="C:\Development\chromedriver.exe"

driver=webdriver.Chrome(driver_path)

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(1)
username=driver.find_element_by_name("username")
username.send_keys(UserId)
password=driver.find_element_by_name("password")
password.send_keys(Passwd)
submit=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
submit.click()
time.sleep(5)
search=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys(Account)
time.sleep(3)
search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)
time.sleep(2)
following=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
following.click()
time.sleep(1)
follow=driver.find_elements_by_css_selector(".sqdOP")
for touch in range(len(follow)):
    print(follow[touch].click())


