"""
演示可视化需求1：折线图开发
"""
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

#处理数据
f_in=open("D:/印度.txt","r",encoding="UTF-8")
in_data=f_in.read()   #美国的全部内容
#去掉不合JSON规范的开头
in_data=in_data.replace("jsonp_1629350745930_63180(","")
#去掉不合JSON规范的结尾
in_data=in_data[:-2]
#JSON转Python字典
in_dict=json.loads(in_data)

#获取trend key
in_trend_data=in_dict['data'][0]['trend']

#获取日期数据，用于x轴，取2020年（到270下标结束）
in_x_data=in_trend_data['updateDate'][:270]

#获取确认数据，用于y轴，取2020年（到270标结束）
in_y_data=in_trend_data['list'][0]['data'][:270]

#生成图表
line=Line()                  #构建折线图对象
#添加x轴数据
line.add_xaxis(in_x_data)           #x轴是公用的，所以使用一个国家的数据即可
#添加y轴数据
line.add_yaxis("印度的确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))  #添加印度的y轴数据

#设置全局选项
line.set_global_opts(
    #标题设置
    title_opts=TitleOpts(title="2020年印度确诊人数折线图",pos_left="center",pos_bottom="-1%"),
)
#调用render方法，生成图表
line.render()
#关闭文件对象
f_in.close()