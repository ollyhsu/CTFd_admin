from selenium import webdriver
from selenium.webdriver.common.by import By
browser=webdriver.Firefox()
url = "http://192.168.2.117/"

def Login(uname, pwd):
    browser.get(url + "/login")
    # print(browser.page_source)
    text_username = browser.find_element(By.ID, "name")
    text_password = browser.find_element(By.ID, "password")
    btn_submit = browser.find_element(By.ID, "_submit")
    text_username.send_keys(uname)
    text_password.send_keys(pwd)
    btn_submit.click()
    return browser
