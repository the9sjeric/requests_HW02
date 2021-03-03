import requests

class Base:

    def __init__(self):
        corpid = "wwd74df2f89ef2a560"
        secret = "NtB_n4sNtWVhcl05wk3YokSWauatjU21hFW0QlODdAs"

        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}"
        r = requests.get(url).json()
        self.token = r.get("access_token")


    def send(self,*args,**kwargs):
        s = requests(*args,**kwargs)
        return s
