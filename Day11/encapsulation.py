# Create a class BankAccount
# Private attributes: __balance , __account_number
class BankAccount:
    def __init__(self, account_number,balance=0):
        self.__balance = balance
        self.__account_number = account_number
        print(f"The account number is: {self.__account_number}")

# Public method to deposit and withdraw money
    def deposit(self,deposit):
        self.__balance += deposit
        print(f"The deposit is: {deposit}")

    def withdraw(self,withdraw):
        self.__balance -= withdraw
        print(f"The withdrawn amount is: {withdraw}")

# Add getter and setter for __balance
    def get_balance(self,):
       return print(f"The previous balance is : {self.__balance}")
        
    def set_balance(self,new_balance):
        self.__balance = new_balance
        print(f"The new balance is: {new_balance}")
    
b1 = BankAccount(123)
b1.deposit(2000)
b1.withdraw(1000)
b1.get_balance()
b1.set_balance(10000)


# Modify BankAccount to use @property and @balance.setter
class BankAccount:
    def __init__(self, account_number,balance=0):
        self.__balance = balance
        self.__account_number = account_number
        print(f"The account number is: {self.__account_number}")

# Public method to deposit and withdraw money
    def deposit(self,deposit):
        self.__balance += deposit
        print(f"The deposit is: {deposit}")

    def withdraw(self,withdraw):
        if self.__balance < withdraw or withdraw < 0 :
            print("Can't be withdrawn")
        else:
            self.__balance -=withdraw
            print(f"The withdrawn amount is: {withdraw}")

# Add property
    @property
    def balance(self):
       return print(f"The previous balance is : {self.__balance}")
    
    @balance.setter
    def balance(self,new_balance):
        if new_balance > 0:
            self.__balance = new_balance
            print(f"The new balance is: {new_balance}")
        else:
            print(f"The number must be greater than 0")

b1 = BankAccount(123)

b1.deposit(2000)
b1.withdraw(-10)
b1.balance
b1.balance = 10000


class Car:
    def __init__(self,fuel_level,engine_status):
        self.__fuel_level = fuel_level
        self.__engine_status = engine_status

    def start_engine(self):
        pass

    def drive(self,drive):
        self.__fuel_level -= drive
        return self.__fuel_level
    
    def set_fuel_level(self,decrease_fuel):
        self.__fuel_level = decrease_fuel
        return self.__fuel_level
    def get_fuel_level(self):
        return self.__fuel_level
    def stop_engine(self):
        pass

c1 = Car(100,1)
c1.get_fuel_level
print(c1.drive(2))
print(c1.get_fuel_level())
print(c1.set_fuel_level(200))







