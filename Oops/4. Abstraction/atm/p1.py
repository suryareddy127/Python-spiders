from abc import ABC,abstractmethod

# abstract class
class ATM(ABC):
    @abstractmethod
    def insert_card(self):
        pass

    @abstractmethod
    def enter_Pin(self,pin):
        pass

    @abstractmethod
    def withdraw_cash(self,amount):
        pass

    @abstractmethod
    def deposit_amount(self,amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def transaction_history(self):
        pass

    @abstractmethod
    def successfully(self):
        pass