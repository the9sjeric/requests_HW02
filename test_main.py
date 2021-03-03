from test_case.test_requests import

corpid = "wwd74df2f89ef2a560"
secret = "NtB_n4sNtWVhcl05wk3YokSWauatjU21hFW0QlODdAs"

def test_aaa():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}"
    r = requests.get(url).json()
    token = r.get("access_token")
    print(token)



requests.post()