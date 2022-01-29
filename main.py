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
            "water": 400,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_sufficient_recourses(drink):
    '''
    Loop over items in drink and compare it with recourses.
    if item of drink is higher than that from recourse return False
    if item of drink is lower return True
    '''
    for item in drink:
        if drink[item] > resources[item]:
            # show message insufficient item (water, milk, coffee)
            print(f"Sorry there is not enough {item}")
            return False
    # return True if loop is done checking all items
    # and none is higher than resource
    return True

def process_coins():
    '''
    Ask the user how much quarters, dimes, nickles, pennies,
    and return the total amount
    '''
    # transform every input to integer for calculation
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    # now return total
    return total

# set machine condition to True
machine_on = True

# prompt user about products and loop the question
while machine_on:
    # choice user what product they want
    choice = input("What whould you like? (espresso/latte/cappuccino)")

    # turn machine off when secret word "off" is used
    if choice == 'off':
        print("Machine is turning off!")
        machine_on = False
    # show report of available products when secret word "report" is used
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    # In all other cases the user selected a product.
    else:
        # create anker point
        drink = MENU[choice]
        # check if there is sufficient recourses only than we can continue
        # send selected drink to compare
        # is_sufficient_recourses returns True or False
        if is_sufficient_recourses(drink["ingredients"]):
            # handle coins and save it in variable
            payment = process_coins()
