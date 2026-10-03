my_str="itheima itcast boxuegu"
count=my_str.count("it")
print(f"字符串{my_str}中有：{count}个it字符")
new_my_str=my_str.replace(" ","|")
print(f"字符串{my_str}，被替换空格后，结果：{new_my_str}")
my_str_list=new_my_str.split("|")
print(f"字符串{new_my_str}，按照|分割后，得到：{my_str_list}")