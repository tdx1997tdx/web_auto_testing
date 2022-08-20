import json


# 读取json文件内容，转化成数据驱动的格式
def load_json(path):
    with open(path) as f:
        data = json.load(f)
    res = []
    for i in data:
        res.append((i["data"], i["story"], i["title"]))
    return res
