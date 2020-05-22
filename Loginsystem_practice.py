'''
this is a practice which is used to establish a sample login system

from fishc forum
'''

user_data = {}

def new_user():
    prompt =  'please enter your username: '
    while True:
        name = input(prompt)
        if name in user_data:
            # 这里的prompt不会影响上边的prompt 吗？
            prompt = 'This username has been used, please use another one:'
            continue
        else:
            break

    passwd = input('please enter the password:')
    user_data[name]=passwd
    print('register successfully! try to login now!!!!')

def old_user():
    prompt = 'please enter your username:'
    while True:
        name = input(prompt)
        if name not in user_data:
            prompt = 'the username you input is not existed, please enter the username again:'
            continue
        else:
            break

    passwd = input('please enter the password:')
    pwd = user_data.get(name) # 返回指定键的值？
    if passwd == pwd:
        print('well come to the homepage of the application, you can quit the application by click x')
    else:
        print('you entered a wrong password!')

def showmenu():
    #这种三个点点的中间的也是字符串吗？？ 是不是三个点点中间的是可以任意换行，
    # 就像我们平时写东西一样， 回车代表换行？
    prompt = '''
|---creat a new account:N/n---|
|---login your account: E/e---|
|---quit the application please: Q/q---|
|---please enter the option---|'''

    while True:
        chosen = False  #这里为什么chosen 要定义为False啊？
        while not chosen: #如果上面定义了是false， 那么这里就应该是说true的时候循环啊
            choice =  input(prompt)
            if choice not in 'NnEeQq':
                print('you entered a wrong option, please try again:')
            else:
                chosen = True #这里chosen判断真假的作用是什么呢？？为什么要判断真假？
                #如果上边的我理解对了 这里不就是true 跳不出循环么？？？ 求解释。 脑壳昏

            if choice == 'q' or choice == 'Q':
                break
            if choice == 'n' or choice == 'N':
                new_user()
            if choice == 'e' or choice == 'E':
                old_user()

showmenu()






