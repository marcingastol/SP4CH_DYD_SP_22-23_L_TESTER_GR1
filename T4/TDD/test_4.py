class Test1:
    def test_1(self):
        zmienna = "Hello World!"
        assert "Hello" in zmienna
    
    def test_2(self):
        zmienna = "Hello World"
        assert "hello" in zmienna