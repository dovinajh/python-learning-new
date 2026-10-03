import random
a=random.randint(1,10)
i=1
while i<=3:
    x=int(input("请输入你猜的数字："))
    if x==a:
        print("你终于猜对了")
        break
    else:
        if x<a:
            print("你猜的太小了")
        else:
            print("你猜的太大了")
        print(f"你还有{3-i}次机会")
        i+=1
else:
    print("三次都猜错了")