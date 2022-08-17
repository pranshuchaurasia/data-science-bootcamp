#import test1
#print(test1)

#obj3=test1.Person1("yoyp","honry",2000)
#print(obj3.yob1)


class Person:
    _name="Pra"
    __surname="chau"
    yob=1998

    def _age(self,current_year):
        return current_year-self.yob
    def __age1(self,current_year):
        return current_year-self.yob

obj = Person()
print(obj._age(2022))
print(obj._Person__age1(2022))

class Employee(Person):
      _name = "PC"
      __surname = "Unknown"
      yob=1992

obj1=Employee()
print(obj1)
print(obj1._age(2022))
print(obj1.yob)
print(obj1._name)
#systerm creates a key value pair for private keyword
print(obj1._Person__surname)
print(obj1._Employee__surname)