# -*- coding: utf-8 -*-

from Output.printf import printf
from Login.login import Login
from Data.data import dataProcess
from User.user import UserAddOpt
from Team.team import TeamAddOpt
from Info.about import PrintInformation

def Model():
    printf("\n----------CTFd Admin----------","yellow")
    printf("\t1.Excel Data Process","blue")
    printf("\t2.Admin Login","blue")
    printf("\t3.Add Users", "blue")
    printf("\t4.Add Teams","blue")
    printf("\t5.Team Choose Users", "blue")
    printf("\t6.Public Notifications","blue")
    printf("\t7.Pressure Test","blue")
    printf("\t8.About","blue")
    printf("\t9.Exit","red")
    printf("--------------------------------", "yellow")
    Model=input("Please Choice Model<<")
    return Model

def main():
    ifContinue = True
    while ifContinue:
        model = Model()
        if model=='1':
            dataProcess()
        if model=='2':
            uname = input("Please enter admin username << ")
            pwd = input("Please enter admin password << ")
            Login(uname, pwd)
        if model=='3':
            UserAddOpt()
        if model=='4':
            TeamAddOpt()
        if model=='5':
            break
        if model=='6':
            break
        if model=='7':
            break
        if model=='8':
            PrintInformation()
        if model=='9':
            ifContinue=False
            printf("Byebye~!","purple")

if __name__ == '__main__':
    main()
