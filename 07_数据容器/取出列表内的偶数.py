mylist1=[1,2,3,4,5,6,7,8,9,10]
mylist2=[]
index=0
while index<len(mylist1):
    if mylist1[index]%2==0:
        mylist2.append(mylist1[index])
    index+=1
print(f"通过while循环，从列表：{mylist1}中取出偶数，组成新列表：{mylist2}")

mylist1=[1,2,3,4,5,6,7,8,9,10]
mylist2=[]
index=0
for index in range(len(mylist1)):
    if mylist1[index]%2==0:
        mylist2.append(mylist1[index])
print(f"通过for循环，从列表：{mylist1}中取出偶数，组成新列表：{mylist2}")