import random as r

class Fish:
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)

    def move(self):
        self.x-=1
        self.y+=1
        print ('位置：',self.x,self.y)

class Salmon(Fish):
    pass

class Shark(Fish):
    def __init__(self):
        Fish.__init__(self)
        #super().__init__()  #super().需要的父类的函数方法
        self.hungry=True

    def eat(self):
        if self.hungry:
            print ('天天吃')
            self.hungry=False

        else:
            print ('不吃')
