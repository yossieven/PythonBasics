
class TestClass:
    def function_1(var):
        return var + 1

    def test_success(self):
        assert TestClass.function_1(4) == 5

    def test_failure(self):
        assert TestClass.function_1(2) == 5
