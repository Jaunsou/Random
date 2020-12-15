import random
answer = random.randint(1,10)
i = 3
while i > 0:
    temp = input("猜个数字:")
    guess = int(temp)
    if guess == answer:
        print("正确")
        print("没奖励")
        break
    else:
        if guess < answer:
            print("小了")
        else:
            print("大了")
        i -= 1
print("游戏结束,答案是"+str(answer))
