# high order functions yaakov soibelman
# question 1
# def apply_to_all(numbers, action):
#     new_list = []
#     for number in numbers:
#         new_list.append(action(number))
#     return new_list

# def double(n):
#     return n * 2

# print(apply_to_all([1, 2, 3], double))
# print(apply_to_all([1, 2, 3], lambda n: n * n))
# print(apply_to_all([1.6, 2.4], round))
    
# question 2    
# def add_ten (price):
#     return price +10
# prices = [20, 75, 120, 45, 90]
# new_prices = list(filter(lambda p: p>50 ,prices))
# print (new_prices)
# new_prices = list(map(add_ten,new_prices))
# print (new_prices)


# # question 3
# words = ["banana", "fig", "cherry", "kiwi"]
# words = sorted (words,key = len)
# longest_word = words[-1]
# print (words,longest_word)

# students = [("Dana", 92), ("Avi", 78), ("Noa", 85)]
# students = sorted (students,key = lambda stud: stud[1],reverse=True)
# for student in students:
#     print (student[0])

# #question 4
# def make_discount(percent):
#     def actuall_discount(price):
#         return price * (1-percent/100)
#     return actuall_discount

# ten_off = make_discount(10)
# half_price = make_discount(50)
# print(ten_off(200))
# print(half_price(200))

# question 5
"""
1. the problem is that in the print already called the double function in the print without passing an argument!

"""

def apply_to_all(numbers, action):
    new_list = []
    for number in numbers:
        new_list.append(action(number))
    return new_list

def double(n):
    return n * 2

print(apply_to_all([1, 2], double))