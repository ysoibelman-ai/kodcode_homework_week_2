# Pure Functions Qeustions

# targil 1
"""
1. is pure because it doesnt change anything globally - the same input will have the same output
2. it's Not pure because it prints to the screen
3. not pure - the function has a side affect that it changes the list "cart"
4. pure - function doesnt change cart
"""

# targil 2
def add_price(total,price):
    new_total = total
    new_total += price
    return new_total

# targil 3
TAX = 1.17
def apply_tax (prices):
    new_prices = []
    for i in range (len(prices)):
        new_prices.append(prices[i] + TAX)
    return new_prices

# targil 4
def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    return total

def show_total(prices):
    total = calculate_total(prices)
    print (f"Total: {total}")

# targil 5
def top_three(numbers):
    new_scores = numbers.copy()
    new_scores.sort()
    return new_scores[-1],new_scores[-2],new_scores[-3]