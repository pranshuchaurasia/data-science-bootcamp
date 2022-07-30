class Person:
    _name="Pranshu"
    __surname="chaurasia"
    yob=1998

obj = Person()
print(obj)

#inheritance

class Employee(Person):
      pass

obj1=Employee()
print(obj1)
print(obj1.yob)
print(obj1._name)
#systerm creates a key value pair for private keyword
print(obj1._Person__surname)