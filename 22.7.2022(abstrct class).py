from abc import ABC,abstractmethod
class a:
    @abstractmethod
    def p(self):
        pass
class b(a):
    def p(self):
        print("abstacted class")

ob=b()
ob.p()
