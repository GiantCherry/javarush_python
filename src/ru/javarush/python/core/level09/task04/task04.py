# Банкир.

# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.

# Напишите тут ваш код
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.accaunt_number = account_number
        self.initial_balance = initial_balance

    def deposit(self, amount):
        self.initial_balance += amount

    def withdraw(self, amount):
        if self.initial_balance >= amount:
            self.initial_balance -= amount

account = BankAccount(777, 2310)

account.deposit(50)
account.deposit(210)
account.withdraw(70)
account.withdraw(700)

print(account.initial_balance)