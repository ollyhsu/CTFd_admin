# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
import pandas as pd
from Login.login import browser,url

def addTeam(username, password):
    browser.get(url + "/admin/teams/new")
    text_username = browser.find_element(By.ID, "name")
    text_password = browser.find_element(By.ID, "password")
    btn_submit = browser.find_element(By.ID, "update-team")
    text_username.send_keys(username)
    text_password.send_keys(password)
    btn_submit.click()
    return browser

def TeamAddOpt():
    d2 = pd.read_excel("./Data/result.xlsx",'团队')
    for i in range(0, len(d2)):
        Team_name = str(d2.iloc[i][0])
        Team_pwd = str(d2.iloc[i][1])
        addTeam(Team_name, Team_pwd)
        print("团队", Team_name, "添加成功")
    print("所有团队添加完成！")
