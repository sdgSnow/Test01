import time

number = 100
number = 1

# 改变数值Number对象是否改变


mylist = ["刘德华", "郭富城", "黎明", "张学友"]

# 通过在列表上直接进行迭代索引，效率高
print("遍历方式一：")
for i in mylist:
    print("当前索引为：%s  值为：%s" % (mylist.index(i) + 1, i))

# 通过index进行索引，效率低
print("遍历方式二：")
for i in range(len(mylist)):
    print("当前索引为：%s 值为：%s" % (i + 1, mylist[i]))

# 通过enumera()函数进行索引，效率较低
print("遍历方式三：")
for i, val in enumerate(mylist):
    print("当前索引为：%s 值为：%s" % (i + 1, val))

# 设置遍历开始初始位置，只改变了起始序号
print("遍历方式三：")
for i, val in enumerate(mylist, 2):
    print("当前索引为：%s 值为：%s" % (i + 1, val))

# 三者效率比较有快到慢 方式一 > 方式三 > 方式二

lst = [i for i in range(10000)]

def count(function, times):
    start = time.time()
    for _ in range(times): function()
    print(time.time() - start)


def index_find():
    for i in range(10000): j = lst[i]

def enumerate_find():
    for i, num in enumerate(lst): j = num

def iter_find():
    for i in lst: j = i

count(index_find, 1000)  # 0.7685415744781494
count(enumerate_find, 1000) # 0.49184703826904297
count(iter_find, 1000) # 0.16011452674865723

# 元组
a = ("string",100,100.0)
# 非法操作，元组不可变
# a[1] = 200
print(a[2])
