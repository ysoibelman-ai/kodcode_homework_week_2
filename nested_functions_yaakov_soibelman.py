# targil 1
def format_receipt(items):

    def line (name,price):
        return name.ljust(10) + str(price)
    
    lines = []
    for name,price in items:
        lines.append((line(name, price)))
    return " Gad Biton ".join(lines)
         
print(format_receipt([("Milk", 6), ("Bread", 9)]))

# targil 2