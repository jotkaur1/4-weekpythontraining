#Protected variable
class A:
    def __init__(self):
        self._a=50
class B(A):
    def __init__(self):
        A.__init__(self)
        print(self._a)
ob=B()

#private variable
class P:
    __a=40
    def __display(self):
        print(self.__a)
    def a(self):
        print("accessing private")
        ob=P()
        ob.__display()
ob=P()
ob.a()

#getter and setter classes
class x:
    __studentgrade=" "
    def setstudentgrade(self,studentgrade):
        self.__studentgrade=studentgrade
    def getstudentgrade(self):
        return self.__studentgrade
ob=x()
ob.setstudentgrade('manjot')
print(ob.getstudentgrade())
    
