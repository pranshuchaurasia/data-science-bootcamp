
class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show account opening status")
    def deposite(self):
        print("This will show deposit account")
    def test(self):
        print("This is a test method from bank class")

class HDFC_bank():
    def hdfc_to_icici(self):
        print("It will show transaction from hdfc to icici bank ")
    def test(self):
        print("This is a test method from hdfc_bank class")

class ineuron_bank:
    def account_status_icici(self):
        print("This is an account status from ineuron to icici")

class icici(bank,HDFC_bank, ineuron_bank):
    pass


i=icici()
i.hdfc_to_icici()
i.transaction()
i.account_opening()
i.deposite()
#if method name is same and we try to call multiple inheritance, it will use the class which is passed first
i.test()

i.account_status_icici()

