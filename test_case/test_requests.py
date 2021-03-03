import requests

"""新增用户"""
def test_add_menber():
        jsonadd = {
                "userid": "reqadd001",
                "name": "阿伊Q",
                "mobile": "+86 13800000225",
                "department": [1]
        }
        urladd = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        radd = requests.post(url=urladd,json=jsonadd)
        print(radd.text)

"""修改用户信息"""
def test_modify_menber():
        jsonmodify = {
                "userid": "reqadd001",
                "position": "后台工程师"
        }
        urlmodify = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
        rmodify = requests.post(url=urlmodify,json=jsonmodify)
        print(rmodify.text)

"""查询用户信息"""
userid = "reqadd001"
def test_query_menber():
        urlquery = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}"
        rquery = requests.get(urlquery)
        print(rquery.text)

"""删除用户"""
def test_del_menber():
        urldel = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}"
        rdel = requests.get(urldel)
        print(rdel.text)