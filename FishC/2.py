import random
secret = random.randint(1,10)
print("-------练习1------")
temp =input("随便想个数：")
guess =int(temp)
if guess==secret:
    print("对了！")
    print("但没奖！")
i=5
while guess!=secret and i!=0:
    i=i-1
    if guess>secret:
        print ("大了")
    else:
        print ("小了")
    temp =input("重新想个数：")
    guess =int(temp)
    
print("对了！")
print("但没奖！")    
print("over")
