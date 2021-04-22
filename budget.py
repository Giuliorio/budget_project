class Category:
    def __init__(self, category, amount):
        self.category = category
        self._amount = amount
    
    @property
    def check_balance(self):
        return print(f"The current balance is: {self._amount}")
    
    def deposit(self, amount):
        self._amount += amount
        return print(f"You have deposited {amount} in {self.category} category. Balance is now {self._amount}")
    
    def withdraw(self, amount):
        self._amount -= self.actual(amount)
        return print(f"You have withdrawn {amount} in {self.category} category. Balance is now {self._amount}")
    
    def transfer(self, amount, category):
        actual = self.actual(amount)
        self.withdraw(actual)
        category.deposit(actual)
        return print("Transfer successful")
    
    def actual(self, amount):
        return min(amount, self._amount)
    
food_category = Category("Food", 300)
clothing_category = Category("Clothing", 150)
car_category = Category("Car", 100)