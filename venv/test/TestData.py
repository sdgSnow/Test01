class Data():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printData(self):
        print("我的名字叫：%s 年龄是：%s" % (self.name,self.age))

# data2 = Data()
data = Data("沈道固",25)
data.printData()