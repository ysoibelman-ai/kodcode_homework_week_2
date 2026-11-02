# Scope Yaakov Soibelman
# targil 1
"""
1. an error becasue the global area doesnt recognize the var message
"""
# def welcome(name):
#     message = "Welcome " + name
#     return message
# final_message = welcome("Dana")
# print(final_message)
# print(final_message)


# targil 2

"""
1: local in first
2: global
3: global
"""

# targil 3
"""
UnboundLocalError because the function doesnt have access to the variable count
"""
def add_one(count):
    return count +1
count = 0
count = add_one(count)

# targil 4
"""
TypeError because list was changed to be an actual list and now it cannot be used as built in method
this is because python looks first in the global for the variable before built in names. 

"""

list_ = [1, 2, 3]
numbers = list(range(5))

# targil 5


def add_cart(price):
    return cart + [price]

def total_prices(cart):
    return sum(cart)

cart = []
cart = add_cart(100)
cart = add_cart(50)
print (cart, total_prices(cart))