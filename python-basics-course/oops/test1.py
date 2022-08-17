class Person:
    def __init__(self,name,surname,emailid, yob):
        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.yob=yob
    def age(self,current_year):
        return(current_year- self.yob)



ross_var=Person("Ross","Peterson","ross@gmail.com", 1997)
print(ross_var.name)
print(ross_var.surname)

print("Hello world1")

print(ross_var.age(2022))