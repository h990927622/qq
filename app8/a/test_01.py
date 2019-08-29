import allure


class Test_01:
    @allure.step("这是001测试方法")
    def test_01(self):
        print("11111111")
        assert True
