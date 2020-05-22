'''
this is a practice of dict from fishC forum
'''


print('§---欢迎使用通讯录程序---§')
print('§---1：查询联系人资料---§')
print('§---2：添加新的联系人---§')
print('§---3：删除已有联系人---§')
print('§---4：退出通讯录程序---§')


contacts = dict()

while 1:
    instr = int(input('\n请输入相关的指令代码：'))

    if instr == 1:
        name = input('请输入联系人姓名')
        if name in contacts:
            print(name+':' + contacts[name])
        else:
            print('没有该联系人')

    if instr == 2:
        name = input('请输入联系人姓名')
        if name in contacts:
            print('联系人已经存在-->>', end='') # end='' 是末尾不换行的意思哈
            print(name+':'+contacts[name])
            if input('是否修改用户资料(YES/NO):')=="YES":
                contacts[name]=input('请输入用户电话号码')
        else:
            contacts[name]=input('请输入新用户电话号码')

    if instr == 3:
        name = input('请输入要删除的联系人姓名：')
        if name in contacts:
            del(contacts[name]) # you also can use dict.pop(). del here is used to delete a element in dict
        else:
            print('您输入的用户不存在喔喔喔哦')

    if instr == 4:
        break

print('---thank you for using this application---')



