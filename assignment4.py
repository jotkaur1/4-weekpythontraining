#Example 1
from abc import ABC, abstractmethod
class Animal(ABC):
  @abstractmethod
  def eat1(self):
           pass
  @abstractmethod
  def eat2(self):
      pass
class Tiger(Animal):
  def eat1(self):
    print("Tiger implementation ...")
class lion(Tiger):
  def eat2(self):
    print("lion implementation ...")
t = lion()
t.eat1()
t.eat2()
'''output
Tiger implementation ...
lion implementation ...'''




#Example 2
from abc import ABC, abstractmethod
class AbstractClassExample(ABC):
  def __init__(self, value):
    self.value = value
    super().__init__()
 
  @abstractmethod
  def do_something(self):
    pass
 
class DoAdd(AbstractClassExample):
  def do_something(self):
            return self.value + 42
 
class DoMul(AbstractClassExample):
 
  def do_something(self):
    return self.value * 42
 
x = DoAdd(10)
y = DoMul(10)
print(x.do_something())
print(y.do_something())
'''output:
52
420'''


#Example 3

def status(age):
 	if age < 0:
 		raise ValueError("Only positive integers are allowed")
 	if age>22:
 		print("eligible for mrg")
 	else:
 		print("not eligible for mrg try after some time")
try:
 	num = int(input("Enter your age: "))
 	status(num)
except ValueError:
 	print("Only positive integers are allowed you ......")
finally:
 	print("finally block....")
'''output:
Enter your age: 20
not eligible for mrg try after some time
finally block....'''


#Example 4

class NegativeAgeException(RuntimeError):
 	def __init__(self, age):
 		super().__init__()
 		self.age = age
def status(age):
 		if age < 0:
 			raise NegativeAgeException("Only positive integers are allowed")
 		if age>22:
 			print("Eligible for mrg")
 		else:
 			print("not Eligible for mrg....")
try:
 	num = int(input("Enter your age: "))
 	status(num)
except NegativeAgeException:
 	print("Only positive integers are allowed")
except:
 	print("something is wrong")
'''output
Enter your age: 30
Eligible for mrg'''


#Example 5:

class TooYoungException(Exception):
    def __init__(self,age):
        self.age=age
class TooOldException(Exception):
    def __init__(self,age):
        self.age=age
try:
    age=int(input("Enter Age:"))
    if age<18:
        raise YoungException("Plz wait some time ")
    elif age>65:
        raise OldException("Your age too old")
    else:
        print("we will find one girl soon")
except YoungException as e:
 	print("Plz wait some time ")
except OldException as e:
 	print("Your age too old ")
'''output
Enter Age:36
we will find one girl soon
'''


