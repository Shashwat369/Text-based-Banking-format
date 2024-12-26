class BankAccount:
    def __init__(self, name, initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully!")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Invalid or insufficient funds.")

    def check_balance(self):
        print(f"Your current balance is ₹{self.balance}.")

def main():
    print("Welcome to the Text-Based Banking System!")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                amount = float(input("Enter the amount to deposit: ₹"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == 2:
            try:
                amount = float(input("Enter the amount to withdraw: ₹"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == 3:
            account.check_balance()
        elif choice == 4:
            print("Thank you for using our banking system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
