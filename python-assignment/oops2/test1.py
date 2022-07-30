#from test2 import Person
# import utils.util1  #First method to import modules and packages in pythons; second method below
from utils.util1 import Person2

obj=Person2("rohan","tibrewal",1324)
print(obj.yob1)
class Person1:
    def __init__(self,name,surname,yob):
        self.name1=name
        self.__surname1=surname
        self.yob1=yob
# __ (double underscore) means private
# - (single underscore) means protected

pran=Person1("pranshu","chaurasia", 1990)
print(pran.name1)
print(pran._Person1__surname1)
