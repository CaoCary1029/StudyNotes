import allure
import pytest


class TestAllure:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试步骤1")
    def test_allure_001(self):
        allure.attach('test_allure', '第一个测试方法')
        print("test_allure_001")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试步骤2")
    def test_allure_002(self):
        allure.attach('test_allure', '第二个测试方法')
        print("test_allure_002")

    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step(title="这是一个登录测试")
    def test_allure_003(self):
        allure.attach('userName', 'cary')
        allure.attach('password', '123456')
        print("test_allure_003")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是一个测试步骤4")
    def test_allure_004(self):
        allure.attach('test_allure', '第四个测试方法')
        print("test_allure_004")

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="这是一个测试步骤5")
    def test_allure_005(self):
        allure.attach('test_allure', '第五个测试方法')
        print("test_allure_005")
