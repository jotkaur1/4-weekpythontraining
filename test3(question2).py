abc import ABC, abstractmethod
class polygon(ABC):
    def common(self):
        print("This is a concrete method")
    @abstractmethod 
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self,side):
        self.__side=side        
    def area(self):
        return self.__side*self.__side    
    def perimeter(self):
        return 4*self.__side       


class Rectangle(Shape):
    def __init__(self,length,breath):
        self.__length=length
        self.__breath=breath        
    def area(self):
        return self.__length*self.__breath    
    def perimeter(self):
        return 2*(self.__length+self.__breath)
S1=Square(4)
print(S1.common())
print(S1.area())
print(S1.perimeter())
R1=Rectangle(2,4)
print(R1.common())
print(R1.area())
print(R1.perimeter())

a= int(input("enter the sides of polygon"))
print("enter the length of sides")
for i in range(a+1):
    l=float(input)

    
