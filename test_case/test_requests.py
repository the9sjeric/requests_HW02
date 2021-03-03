from api.contect import Contect
import pytest


class TestCase:

        def setup(self):
                self.contect = Contect()

        @pytest.mark.parametrize("userid, name, phone,department",[("req999", "999", 13866669999, [1])])
        def test_add_menber(self,userid, name, phone,department):
                r = self.contect.add_menber(userid, name, phone, department)
                assert r.get("errcode") == 0

        @pytest.mark.parametrize("userid, position",[("req666","测试工程师001")])
        def test_modify_menber(self,userid,position):
                r = self.contect.modify_menber(userid,position)
                assert r.get("errcode") == 0

        @pytest.mark.parametrize("userid",[("req888")])
        def test_del_member(self,userid):
                r = self.contect.del_menber(userid)
                assert r.get("errcode") == 0