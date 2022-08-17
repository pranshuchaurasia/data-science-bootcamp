class ineuron:
    def student(self):
        print("The details of all students")
    def acivers(self):
        print("People completed the courses")
    def hall_of_fame(self):
        print("People in hall of fame")

class ineuron_vision(ineuron):
    def student(self):
        print("This is a filtered student list")


iv =ineuron_vision()
iv.student()
