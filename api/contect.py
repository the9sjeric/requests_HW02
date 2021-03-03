from api.base import Base




class Contect(Base):

        def add_menber(self, userid: str, name: str, phone, department: list):
                jsonadd = {
                        "userid": userid,
                        "name": name,
                        "mobile": phone,
                        "department": department
                }
                urladd = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?"
                return self.send('post', urladd, json=jsonadd)

        def modify_menber(self, userid: str, position:str):
                jsonmodify = {
                        "userid": userid,
                        "position": position
                }
                urlmodify = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?"
                return self.send('post', urlmodify, json=jsonmodify)

        def query_menber(self, userid:str):
                urlquery = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
                return self.send('get', urlquery)


        def del_menber(self,userid:str):
                urldel = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
                return self.send('get', urldel)
