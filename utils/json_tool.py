import json


# ��ȡjson�ļ����ݣ�ת�������������ĸ�ʽ
def load_json(path):
    with open(path) as f:
        data = json.load(f)
    res = []
    for i in data:
        res.append((i["data"], i["story"], i["title"]))
    return res
