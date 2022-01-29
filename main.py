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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

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