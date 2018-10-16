print("name:%s age:%s" % ("sdg", 25))
# 下面是否可以打印
print("name:" + "sdg" + "age:" + str(25))

i = 0
while True:
    name = input("请输入你的名字：")
    if name == "shendaogu":
        print("登陆成功")
        break
    else:
        print("登录失败")
        continue
# 不支持switch语句，添加elif
