from config.config import cookie


# 解析cookie内容，转化为格式
def get_cookie_dict():
    res = []
    for i in cookie.split(";"):
        line = i.strip().split("=")
        res.append({"name": line[0], "value": line[1]})
    return res
