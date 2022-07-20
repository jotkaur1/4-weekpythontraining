##########overriding 
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
