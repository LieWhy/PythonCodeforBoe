import datetime


class MyClass:
    i = 123456
    time = datetime.datetime.now()

    def f(self):
        return 'hello world'

    def f1(self):
        return datetime.datetime.now()

    def __init__(self):
        self.data = []


x = MyClass()

print("MyClass类的属性i为：", x.i)
print("MyClass类的方法f为：", x.f())
print("MyClass类的方法f1为：", x.f1())
print("MyClass类的方法__init__为：", x.__init__())
print(datetime.datetime.now())
