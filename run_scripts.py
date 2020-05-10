from test_scripts.Calculate import Calculate
import pytest
from test_data.GetData import get_calculate_data

calculate = get_calculate_data()


class TestCalculate(object):

    def setup(self):
        self.calculate = Calculate()
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize("oper,a,b,expect,desc", get_calculate_data())
    def test_add(self, oper, a, b, expect, desc):
        if hasattr(self.calculate, oper):
            func = getattr(self.calculate, oper)
        else:
            print("该方法不存在%s" % oper)
        assert expect == func(a.get("value"), b.get("value"))
