
class bank:
    def transaction(self):
        print("Total transaction value")
    def account_opening(self):
        print("This will show account opening status")
    def deposite(self):
        print("This will show deposit account")

class HDFC_bank():
    def hdfc_to_icici(self):
        print("It will show transaction from hdfc to icici bank ")

class icici(bank,HDFC_bank):
    pass

i=icici()
i.hdfc_to_icici()
i.transaction()
i.account_opening()
i.deposite()