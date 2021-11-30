from xpinyin import Pinyin
import pandas as pd
import random
import string

def dataProcess():
    df1 = data = pd.read_excel("./Data/demo.xlsx")
    df2 = pd.DataFrame(index= range(len(data)),columns=['团队名称','团队密码'])
    df2.iloc[:,0] = data.iloc[:,0]
    df2 = df2.drop_duplicates(subset=None, keep='first', inplace=False)

    # 姓名转用户名拼音
    df1["用户名"] = None
    for i in range(0, len(df1)):
        name = str(df1.iloc[i][1])
        p = Pinyin()
        pyresult = p.get_pinyin(name)
        pyresult = pyresult.replace('-', '')
        df1.iloc[i, len(df1.columns)-1] = pyresult

    # 生成用户随机密码
    df1["用户密码"] = None
    for i in range(0, len(df1)):
        userpwd = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        df1.iloc[i, len(df1.columns)-1] = userpwd

    # 处理团队信息
    for i in range(0,len(df2)):
        teampwd = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        df2.iloc[i,len(df2.columns)-1] = teampwd

    # 将处理数据写入用户表
    writer = pd.ExcelWriter('./Data/result.xlsx')
    df1.to_excel(writer,'用户',index=False)
    df2.to_excel(writer,'团队',index=False)
    writer.save()
    print("数据处理完成，用户随机密码保存在xls中！")
