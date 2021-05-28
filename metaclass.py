class Test_Class:
    y = 20


ob1 = Test_Class()
class1 = type('Python', (Test_Class, ), {'x' : 10})
ob2 = class1()
print(ob2.y)


class Meta(type):
    pass


class Education(metaclass=Meta):
    pass


print(type(Education))


class MetaTwo(type):
    def __new__(self, name, bases, attr):
        print("new is called")

    def __init__(self, name, bases, attr):
        print("This")


class Python(metaclass=MetaTwo):
    print("Hello")


# ob3 = Python()
