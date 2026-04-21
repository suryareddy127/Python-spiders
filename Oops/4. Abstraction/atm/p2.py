from p1 import ATM

class SBI_ATM(ATM):
    balance = 2000
    def insert_card(self,i):
        self.i =i
        if i == "insertCard":
            print("Card Inserted")
        else:
            print("First insert the card")
        

    def enter_Pin(self, pin):
        self.pin = pin
        if pin!=0 and pin>=1000 and pin<=9999 :
            print("pin verified")
        else:
            print("enter the correct pin")
    
    def withdraw_cash(self, amount):
        self.amount =amount
        if amount>=500 and amount<=self.balance:
            print("proceed for withdraw")
            print(f"{amount}  withdraw Success....")
        else:
            print(f"Enter the amount of minimum 500 or below the {self.balance} balance")

    def deposit_amount(self, amount):
        self.amount= amount
        print(f"{amount}  deposited Success....")
    
    def check_balance(self):    
        print(f"Balance viewed: {self.balance-self.amount}")
    
    def transaction_history(self):
        print("Transactions history")
    
    def payment_success(self):
        print("Successfully Completed")
    


mytrans = SBI_ATM()
mytrans.insert_card("insertCard")
mytrans.enter_Pin(int(input("pin: ")))
mytrans.withdraw_cash(int(input("withdrwal amount: ")))
mytrans.check_balance()
mytrans.payment_success()