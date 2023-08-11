class account:
    def __init__(self,name):
        """
        Function of assigning name with balance of 0
        :param name: Person;s name
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        """
        Function of incrementing account balance
        :param amount: increment amount
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self,amount):
        """
        Function of decrement account balance
        :param amount: decrement amount
        """
        if amount < 0 or amount > self.__account_balance:
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name