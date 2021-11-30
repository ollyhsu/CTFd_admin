from Output.printf import printf
from selenium import webdriver
def PrintInformation():
    Information='''
    Version:v0.1
    Date:2021.11.30
    Github:Vicosna
    Welcome to My Github,to make our world better!
    Enter M to For More...'''
    printf("\n"+Information,'purple')
    URL = 'https://github.com/vicosna/'
    ifForMore=input()
    if ifForMore=='M':
        printf("visiting "+URL,'blue')
        browser = webdriver.Firefox()
        browser.get(URL)

    input("Enter to continue...\n\n")