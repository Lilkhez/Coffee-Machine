from materials import MENU, resources


def process_coins():
    """ Process coins."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_success(money_received, drink_cost):
    """Check transaction successful?"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded")
        return False


def check_resources(order_ingredient):
    """Check resources sufficient?"""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry there is no enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    """Make Coffee."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


profit = 0
# Prompt user by asking “What would you like? (espresso/latte/cappuccino)
flag = True
while flag:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        flag = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_success(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
