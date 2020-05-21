# import easygui
# easygui.msgbox("hello")


# from easygui import *
#
# msgbox("嗨， 小美女")

# import easygui as g
#
# g.msgbox("嗨，小帅哥")


import sys

import easygui as g

while 1:
    g.msgbox("嗨， 欢迎进入第一个界面小游戏")
    msg="请问你希望在这里学习到什么只是呢？"
    title="小游戏互动"
    choices=["love", "programming", "OMG", "piano"]

    choice=g.choicebox(msg,title,choices)

    # we need to convert choice to string, in case the user cancelled the choice, and we got None.

    g.msgbox("你的选择是：" + str(choice), "结果")

    msg="do you want to replay this game?"
    title="please select"

    # show a Continue/Cancel dialog
    if g.ccbox(msg,title):
        # user chose continue
        pass
    else:
        # user chose Cancel
        sys.exit(0)