# functions deep yaakov soibelman

# targil 1
def  make_greeting(name, greeting="Hello", punct="!"):
    return f"{greeting}, {name}{punct}"

# targil 2

def average(*numbers):
    if len (numbers) == 0:
        raise ValueError ("need at least one number")
    return sum(numbers) / len (numbers)

# targil 3
def format_profile(name, **details):
    printout = f"{name}:"
    for key,value in details.items():
        printout += f" {key}={value} "
    return printout

#targil 4
products = [("Laptop", 3500), ("Mouse", 80), ("Desk", 900)]
for product, price in sorted(products, key = lambda prod: prod[1] ):
    print (product, price)

#targil 5
"""
1. milk and bread will be printed because in python becasue we set cart = [] its value will be stored every time we call the function
"""
def add_item(item, cart=[]):
    new_cart = cart.copy()
    new_cart.append(item)
    return new_cart