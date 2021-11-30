# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import pandas as pd
from Login.login import browser,url

def addUser(username, email, password, affiliation):
    browser.get(url + "/admin/users/new")
    text_username = browser.find_element(By.ID, "name")
    text_useremail = browser.find_element(By.ID, "email")
    text_password = browser.find_element(By.ID, "password")
    text_affiliation = browser.find_element(By.ID, "affiliation")
    btn_submit = browser.find_element(By.ID, "update-user")
    text_username.send_keys(username)
    text_useremail.send_keys(email)
    text_password.send_keys(password)
    text_affiliation.send_keys(affiliation)
    btn_submit.click()
    return browser

def UserAddOpt():
    d1= pd.read_excel("./Data/result.xlsx",'用户')
    for i in range(0, len(d1)):
        User_name = str(d1.iloc[i][4])
        User_email = str(d1.iloc[i][3])
        User_pwd = str(d1.iloc[i][5])
        User_affiliation = str(d1.iloc[i][1])+"-"+str(d1.iloc[i][2])
        addUser(User_name, User_email, User_pwd, User_affiliation)
        print("用户", User_name, "注册成功")
    print("用户全部添加完成！")
    return UserAddOpt
