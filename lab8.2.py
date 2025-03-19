import random

random_numbers = {random.randint(15, 45) for i in range(10)}

count_less_than_30 = sum(1 for num in random_numbers if num < 30)

count_less_than_35 = {num for num in random_numbers if num <= 35}

print("Original Set:", random_numbers)
print("Count of numbers less than 30:", count_less_than_30)
print("Set after removing numbers greater than 35:", count_less_than_35)