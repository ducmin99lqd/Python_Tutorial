class father():
    def method1(self):
        print(" method1")
class child(father):
    def method2(self):
        print("method 2")
a=child()
a.method1()
a.method2()