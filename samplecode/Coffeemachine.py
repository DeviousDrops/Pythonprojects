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

money = 0

def report():
    global resources, money
    for item, quantity in resources.items():
        print(f"{item}: {quantity}")
    print(f"Money: ${money}")

def check(a):
    global MENU, resources
    for key, value in MENU[a]['ingredients'].items():
        if value > resources[key]:
            return False
    return True

def calc(ch, s):
    types = {'pennies': 0.01, 'dimes': 0.05, 'nickels': 0.10, 'quarters': 0.25}
    total = 0
    for i in types:
        p = int(input(f"How many {i}? "))
        total += types[i] * p

    global MENU, money, resources
    if MENU[ch]['cost'] > total:
        print("Not enough money, everything is refunded.")
    else:
        change = total - MENU[ch]['cost']
        print(f"Change: ${change:.2f}")
        money += MENU[ch]['cost']
        for i in resources:
            resources[i] -= MENU[ch]['ingredients'][i]
    return total

def output():
    global money, resources
    while True:
        choice = input("What would you like?: ").lower()
        if choice in MENU:
            if check(choice):
                total_money = calc(choice, money)
                print(f"Thank you for your purchase! Total money inserted: ${total_money:.2f}")
            else:
                print("Sorry, we are out of some ingredients.")
        elif choice == 'report':
            report()
        elif choice == 'off':
            exit()

output()