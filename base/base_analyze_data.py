import yaml
import os


def analyze_data(file_name,key):
    #获取当前路径，拼接到目标路径，然后拼接文件名
    data_path = "." + os.sep + "data" + os.sep
    with open(data_path + file_name, "r", encoding="utf-8") as f:
        #通过key加载数据
        data = yaml.load(f)[key]
        data_list = []
        #将测试数据循环加载到list，然后返回
        for i in data.values():
            data_list.append(i)
        return data_list


