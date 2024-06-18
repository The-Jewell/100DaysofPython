MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 100,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    """Prints the resources report to the screen"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money ${resources['money']} ")


def resources_sufficient(order):
    """checks to see if there is enough resources to complete the order"""
    for item in order:
        if order[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_money():
    """processes the money entered by the user"""
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def is_transaction_completed(payment_amount, drink_cost):
    """checks to see if the payment is enough to cover the drink,
     if so  gives back change and update money in the resource report"""
    if payment_amount >= drink_cost:
        change = round(payment_amount - drink_cost, 2)
        print(f"Here is your change. ${change}")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry, that is not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """takes the order and removes the resources required and updates the report,
    "delivers" the drink to the user"""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕️")


machine_on = True

while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print_report()
    else:
        drink = MENU[user_choice]
        print(drink)
        if resources_sufficient(drink["ingredients"]):
            payment = process_money()
            if is_transaction_completed(payment, drink["cost"]):
                make_coffee(user_choice, drink['ingredients'])






