class Person2:
    def __init__(self,name,surname,yob):
        self.name1=name
        self.__surname1=surname
        self.yob1=yob
# __ (double underscore) means private
# - (single underscore) means protected

#pran=Person2("pranshu","chaurasia", 1990)
#print(pran.name1)
#print(pran._Person2__surname1)