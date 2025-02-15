

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
COIN_VALUES ={'quarters': 0.25,
        'dimes': 0.10,
        'nickles': 0.05,
        'pennies': 0.01}

profit = 0


def maker_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(user_drink):

    for item in user_drink['ingredients']:
        if user_drink['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    money_received = 0
    for coin in COIN_VALUES:
        coin_num = int(input(f"How many {coin}?:"))
        money_received += coin_num * COIN_VALUES[coin]
    return money_received




def is_transaction_successful(money_received, drink_cost ):
    global profit
    if money_received >= drink_cost:

        change = round(money_received - drink_cost,2)
        print(f"Here is your change:  ${change}.")
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.  Money refunded.")
        return False


def make_coffee(drink_name, user_drink):
    #deduct the required ingredients from resources
    for item in user_drink['ingredients']:
        resources[item] -= user_drink['ingredients'][item]
    print(f"Here is your {drink_name} . Enjoy!")

is_on = True

while is_on == True:
    # TODO: 1  Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    choice = input(f"What would you like? (espresso/latte/cappuccino)  ").lower()

    #TODO 2: Turn off the Coffee Machine by entering “off" to the prompt.
    if choice == "off":
        is_on = False

    #TODO 3: Print report.
    elif choice == "report":
        maker_report()


    else:

        #TODO 4: Check resources sufficient?
        user_drink = MENU.get(choice)
        if user_drink:
            enough_resource = is_resource_sufficient(user_drink=user_drink)
            if enough_resource:
                # TODO 5: Process coins.
                payment = process_coins()
                #TODO 6: Check transaction successful?
                transaction_success = is_transaction_successful(payment,user_drink['cost'])

                # TODO 7: Make Coffee
                if transaction_success == True:
                    make_coffee(choice, user_drink)

        else:
            print("Invalid choice. Please select again.")


