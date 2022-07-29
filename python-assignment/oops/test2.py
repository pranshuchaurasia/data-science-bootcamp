class Person:
    def age(self,current_year, yob):
        return(current_year-yob)
    def mailid(self,emailid):
        print("Your email id is: ", emailid)
    def ask_name(self):
        name=input("Enter your name")
        return name
    def ask_dob(self):
        dob=input("Tell me your dob")
        return dob

pran=Person()
van=Person()
arch=Person
