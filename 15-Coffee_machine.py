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

def report(m):
    print(f"money : {money} TL")
    for k in resources.keys():
        print(f"{k} : {resources[k]}ml")
        

def change_calculator(ord, kr, lr):
    payment=lr+(kr*0.01)
    cost=MENU[ord]['cost']
    if payment<cost:
        print("Sory, that's not enough money. Money refunded.")
        return money+0
    elif payment>=cost:
        change=payment-cost
        order_control=customer_order(ord)
        if order_control:
            print(f"Here is {change} TL change.")
            return money+payment-change
        else:
            return money+0

def customer_order(ord):
    if MENU[ord]['ingredients']['water']<resources['water']:
        if MENU[ord]['ingredients']['coffee']<resources['coffee']:
            if ord!='espresso' and MENU[ord]['ingredients']['milk']<resources['milk']:
                print(f"Here is your {ord}. Enjoy!")
                resources['water']=resources['water']-MENU[ord]['ingredients']['water']
                resources['milk']=resources['milk']-MENU[ord]['ingredients']['milk']
                resources['coffee']=resources['coffee']-MENU[ord]['ingredients']['coffee']
                return True
            elif ord=='espresso':
                print(f"Here is your {ord}. Enjoy!")
                resources['water']=resources['water']-MENU[ord]['ingredients']['water']
                resources['coffee']=resources['coffee']-MENU[ord]['ingredients']['coffee']
                return True
            else:
                print("Sorry, there is not enough milk.")            
        else:
            print("Sorry, there is not enough coffee.")
    else:
        print("Sorry, there is not enough water.")

money=0

while True:
    order= input("What would you like? (espresso/latte/cappuccino):")
    if order=='report':
        report(money)
    elif order=='off':
        exit()
    else:
        kurus= float(input("How many kurus:    "))
        lira= float(input("How many lira:    "))
        money=change_calculator(order, kr=kurus, lr=lira)
