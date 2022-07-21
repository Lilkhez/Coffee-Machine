balance = 0


def deposit(amount):
    global balance
    balance += amount
    return amount


def withdraw(amount):
    global balance
    balance -= amount
    return amount


is_on = True
while is_on:
    choice = input("What do you want to do? (withdraw/deposit/check balance/off): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "withdraw":
        cash = float(input("How much do you want to withdraw?: $"))
        if cash > balance:
            print("Insufficient Fund")
        else:
            wi_draw = withdraw(cash)
            print(f"You successfully withdraw ${wi_draw}")
    elif choice == "deposit":
        cash = float(input("How much do you want to deposit?: $"))
        deposit = deposit(cash)
        print(f"You Successfully deposited ${deposit}")
    elif choice == "balance":
        print(f"Your Total balance is ${balance}")
    else:
        print("Invalid Input")
