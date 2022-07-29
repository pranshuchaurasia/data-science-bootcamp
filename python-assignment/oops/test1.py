class Person:
    def __init__(self,name,surname,emailid, yob):
        self.name=name
        self.surname=surname
        self.emailid=emailid
        self.yob=yob


ross_var=Person("Ross","Peterson","ross@gmail.com", 1990)
print(ross_var.name)
print(ross_var.surname)

print("Hello world1")