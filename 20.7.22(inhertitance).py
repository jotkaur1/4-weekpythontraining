class Parent:
     def func1(self):
          print("this is function one")
class Child(Parent):
     def func2(self):
          print(" this is function 2 ")
ob = Child()
ob.func1()
ob.func2()
print()

####multiple#####
class Parent:
   def func1(self):
        print("this is function 1")
class Parent2:
   def func2(self):
        print("this is function 2")
class Child(Parent , Parent2):
    def func3(self):
        print("this is function 3")
 
ob = Child()
ob.func1()
ob.func2()
ob.func3()
print()

#multilevel
class Parent:
      def func1(self):
          print("this is function 1")
class Child(Parent):
      def func2(self):
          print("this is function 2")
class Child2(Child):
      def func3():
          print("this is function 3")
ob = Child2()
ob.func1()
ob.func2()
print()

#heirarchical
class Parent:
      def func(self):
          print("this is function 1")
class Child(Parent):
      def func(self):
          print("this is function 2")
class Child2(Parent):
      def func(self):
          print("this is function 3")
 
ob = Child()
ob1 = Child2()
ob.func()
ob1.func()
print()
#hybrid

class School:
    def func1(self):
        print("This function is in school.")
 
 
class Student1(School):
    def func2(self):
        print("This function is in student 1. ")
 
 
class Student2(School):
    def func3(self):
        print("This function is in student 2.")
 
 
class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")
 
 

object = Student3()
object.func1()
object.func2()

