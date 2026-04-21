from p1 import ATM

class SBI_ATM(ATM):
    def insert_card(self,i):
        self.i =i
        if i == "insertCard":
            print("Card Inserted")
        else:
            print("First insert the card")
        # print(f"successfull {self.i}")

    def enter_Pin(self, pin):
        self.pin = pin
        if pin!=0:
            print("pin verified")
        else:
            print("enter the correct pin")
    
    def withdraw_cash(self, amount):
        return super().withdraw_cash(amount)
    
    def deposit_amount(self, amount):
        return super().deposit_amount(amount)
    
    def check_balance(self):
        return super().check_balance()
    
    def transaction_history(self):
        return super().transaction_history()
    
    def payment_success(self):
        return super().payment_success()
    


mytrans = SBI_ATM()
mytrans.insert_card("insertCard")
mytrans.enter_Pin(1231)
mytrans.withdraw_cash(2000)
mytrans.payment_success