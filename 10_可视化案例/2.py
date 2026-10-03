"""
演示全国疫情可视化地图开发
"""
import  json
from pyecharts.charts import Map
from pyecharts.options import *

#读取数据文件
f=open("D:/疫情.txt","r",encoding="UTF-8")
data=f.read()
#关闭文件
f.close()
#取到各省数据
#将字符串json转换为python的字典
data_dict=json.loads(data)       #基础数据字典
#从字典中取出省份的数据
province_data_list=data_dict["areaTree"][0]["children"]
#组装每个省份和确诊人数为元组，并将各省数据都封装入列表中
data_list=[]        #绘图需要用的数据列表
for province_data in province_data_list:
     province_name = province_data["name"]
     province_confirm = province_data["total"]["confirm"]
     data_list.append((province_name, province_confirm))
#构建地图对象
map=Map()
#添加数据
map.add("各省份确诊人数",data_list,"china",name_map={
    "北京市":"北京",
    "天津市":"天津",
    "上海市":"上海",
    "重庆市":"重庆",
    "河北省":"河北",
    "山西省":"山西",
    "辽宁省":"辽宁",
    "吉林省":"吉林",
    "黑龙江省":"黑龙江",
    "江苏省":"江苏",
    "浙江省":"浙江",
    "安徽省":"安徽",
    "福建省":"福建",
    "江西省":"江西",
    "山东省":"山东",
    "河南省":"河南",
    "湖北省":"湖北",
    "湖南省":"湖南",
    "广东省":"广东",
    "海南省":"海南",
    "四川省":"四川",
    "贵州省":"贵州",
    "云南省":"云南",
    "陕西省":"陕西",
    "甘肃省":"甘肃",
    "青海省":"青海",
    "内蒙古自治区":"内蒙古",
    "广西壮族自治区":"广西",
    "西藏自治区":"西藏",
    "宁夏回族自治区":"宁夏",
    "新疆维吾尔自治区":"新疆",
    "台湾省":"台湾",
    "香港特别行政区":"香港",
    "澳门特别行政区":"澳门"
}
)
#设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,           #是否显示
        is_piecewise=True,      #是否分段
        pieces=[
            {"min":1, "max":99,"label":"1-99人","color":"#CCFFFF"},
            {"min":100, "max":999,"label":"100-999人","color":"#FFFF99"},
            {"min":1000, "max":4999,"label":"1000-4999人","color":"#FF9966"},
            {"min":5000, "max":9999,"label":"5000-9999人","color":"#FF6666"},
            {"min":10000, "max":99999,"label":"10000-99999人","color":"#CC3333"},
            {"min":100000, "label":"100000+","color":"#990033"},
        ]
    )
)
#绘图
map.render("全国疫情地图.html")