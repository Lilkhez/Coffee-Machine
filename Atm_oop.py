class Account:
    def __init__(self):
        self.balance = 0

    def deposit(self, dep):
        self.balance += dep

    def withdraw(self, with_draw):
        self.balance -= with_draw


my_account = Account()
quit_sim = True
while quit_sim:
    choice = input("What do you want to do: (deposit/withdraw/balance/off): ")
    if choice == "deposit":
        depo = int(input("Enter the amount you want to deposit: $"))
        my_account.deposit(depo)
        print("Deposit successful!")
    elif choice == "withdraw":
        with_dr = int(input("Enter the amount you want to withdraw: $"))
        if my_account.balance > with_dr:
            my_account.withdraw(with_dr)
            print("Withdrawal successful!")
            print(f"You successfully withdrew ${with_dr}")
        else:
            print("Insufficient balance")
    elif choice == "balance":
        print(f"Your balance is ${my_account.balance}")
    elif choice == "off":
        quit_sim = False
    else:
        print("Wrong input!")
