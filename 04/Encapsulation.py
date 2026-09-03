class BankAccount:
    def __init__(self,name,balance,cvv):
        self.name = name
        self._balance = balance
        self.__cvv = cvv
acc1 = BankAccount("Rahul Kumar",100_000)