class ineuron:
    def students(self):
        print("The details of all students")


class class_type:
    def students(self):
        print("Print the class for student")

def ineuron_external(a):
    a.students()

i=ineuron()
j=class_type()
ineuron_external(i)
ineuron_external(j)

def test(a, b):
    return a+b


#print(test(3, 5))
#print(test("flop ", "movie"))
