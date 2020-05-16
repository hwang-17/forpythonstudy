dict1={}
# a=dict1.fromkeys((1,2,3))
dict1.fromkeys((1,2,3))
a=dict1.fromkeys((1,2,3),"Number")




dict1 = dict1.fromkeys(range(32), "good")

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)


for i in dict1.items():
    print(i)


print(dict1[31])

# get 方法：当因为用不存在的key值进行索引的时候有可能因为不存在而报错，用get就可以避免。
print(dict1.get(32))

# 如果不想返回的值时None，可以自定义返回的值
print(dict1.get(32, "NoValue"))
print(dict1.get(31, "NoValue"))

# 如果不知道一个键是否在字典中，可以使用成员资格操作符 in, not in
print(31 in dict1)
print(32 in dict1)

# 清空一个字典
print(dict1.clear())

# 最好不要直接用{}来清空一个字典
a={"name": "haowang"}

b=a

print(b)

a={}
print(a)

# b实质上还是包含了a的contents
print(b)

a=b

print(a)
print(b)

# 将a,b同时清空
a.clear()
print(a)
print(b)

# dict中的copy（）方法(浅拷贝)**浅拷贝的id是不同的：
a={1:"one",2:'two', 3:"three"}
b=a.copy()
c=a

c[4]="four"

print(a)
# 用了点copy的b不会被影响到
print(b)
print(c)
print(id(a),id(b), id(c))


# pop() 和 pop.items: pop是给定键，弹出对应的值。pop.item（）弹出的时键值对(但是popitem()弹出的item是随机的)。

print(a.pop(2))

print(a.popitem())



# setdefault() 方法，跟get方法有一点点类似. 只是说setdefault()在依据健找不到对应的值的时候会自动添加找不到的键值
# 因为"天天"没有， 所以会添加， 这里只添加了健
a.setdefault("天天")
print(a)

# 以下是同时添加键值
a.setdefault(5,"five")
print(a)

# update()是用一个映射关系去更新一个字典
b={"天天":"dog"}
a.update(b)
# 天天的值之前是None， 现在是dog
print(a)


