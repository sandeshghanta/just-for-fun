from splinter import Browser
from selenium import webdriver
import selenium
#driver = webdriver.Chrome()
with Browser('chrome') as browser:
    browser.visit('https://aums-students-am.amrita.edu:8443/cas/login?service=https%3A%2F%2Faums-students-am.amrita.edu%3A8443%2Faums%2FJsp%2FCore_Common%2Findex.jsp')
    browser.find_by_id('username').first.value = "AM.EN.U4CSE16254"
    browser.find_by_id('password').first.value = "get lost"
    browser.find_by_name('submit').click()
    browser.find_by_id('username').first.value = "AM.EN.U4CSE16254"
    browser.find_by_id('password').first.value = "stop staring"
    browser.find_by_name('submit').click()
    browser.execute_script("document.getElementById('oM_m701').style.visibility='visible';")
    #browser.execute_script("document.getElementById('oM_m701').click();")
    input('Press ENTER to exit')
