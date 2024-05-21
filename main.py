from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu1 = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()
a = True
while a:
    option = input(f"What would you like to have? {menu1.get_items()}:")
    if option == "report":
        coffee.report()
        money.report()
    else:
        s = menu1.find_drink(option)
        if s:
            m = coffee.is_resource_sufficient(s)
            if m:
                q = money.make_payment(s.cost)
                if q:
                    coffee.make_coffee(s)
