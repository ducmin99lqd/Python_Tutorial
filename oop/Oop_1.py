class MyClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfun(self):
        if self.age>22:
            print(" Older ")
        else:
            print(" Younger ")
p1=MyClass("duc min",21)
p2=MyClass("minh phuong",23)
print(p1.name)
print(p2.name)

p1.myfun()
p2.myfun()
