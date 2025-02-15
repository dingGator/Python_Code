from oop_coffee_machine_menu import Menu, MenuItem
from oop_coffee_machine__coffee_maker import CoffeeMaker
from oop_coffee_machine__money_machine import MoneyMachine




menu= Menu()
maker = CoffeeMaker()
money = MoneyMachine()


is_on = True
while is_on == True:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}):  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        maker_report = maker.report()
        money_report = money.report()
    else:
        drink = menu.find_drink(choice)
        suf_resource = maker.is_resource_sufficient(menu.find_drink(choice))
        if suf_resource == True:
            item_cost = menu.find_drink(choice).cost
            accept_payment = money.make_payment(menu.find_drink(choice).cost)
            if accept_payment == True:
                coffee = maker.make_coffee(menu.find_drink(choice))




