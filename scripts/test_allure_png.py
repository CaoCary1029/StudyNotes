import allure


class TestAllurePNG:
    def test_add_png(self):
        with open("./chicken.png", "rb") as f:
            allure.attach('错误截图', f.read(), allure.attach_type.PNG)
