import easygui as g
import sys

while 1:
    g.msgbox("欢迎进入第一个界面小游戏","hajime")

    msg="学习Python准备干嘛？"
    title="梦想"
    choices=["nagaiiki","shigoto","nantemo","betsuni"]

    choice=g.choicebox(msg,title,choices)

    g.msgbox("yourchoice:"+str(choice),"kekka")

    msg="wish to restart?"
    title="choice please"

    if g.ccbox (msg,title):
        pass
    else:
        sys.exit(0)
