"""
Targil 1
"""
from prices import apply_discount,add_vat
discounted = apply_discount(200, 10)
final_price = add_vat(discounted)
print("After discount:", discounted)
print("With VAT:", final_price)

"""
Targil 2

import prices
from prices import apply_discount,add_vat
import prices as prc
"""

"""
Targil 3
"""
import math, random
random.seed(1)
print(math.sqrt(81),"\n",math.pi,"\n",random.randint(1, 6) )


"""
Targil 4
1. the bottom printout will aso be printed because when you import a file python runs it and if there is something there globally it will run auto-pilot
2. put the print in the function
"""

"""
Targil 5
"""

from temperature import c_to_f, describe
cities = ["Eilat", "Haifa", "Jerusalem"]
temperatures = [35, 22, 9]

for i in range (3):
    print (f"{cities[i]}: {temperatures[i]} C / {c_to_f(temperatures[i])} - {describe(temperatures[i])}")
