class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print(f"The user name is {self.name} User is a {self.age} with the age of {self.age}")


user1 = User("JOE", 21, "Male")


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0


    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print(f"The balnce in {self.name} 's account is INR{self.balance}")

    def withdrawl(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= self.amount
        print(f"The balnce in {self.name} 's account is INR{self.balance}")

    def view_balance(self):
        print(f"The balnce in {self.name} 's account is INR{self.balance}")


user1 = Bank("JOE", 21, "Male")
user1.deposit(200)
user1.deposit(200)
user1.withdrawl(100)

user1.withdrawl(1000)
user
