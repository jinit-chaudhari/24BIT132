import random

random_integers = [random.randint(1, 100) for _ in range(20)]

print("list:", random_integers)

num = int(input("Enter a number to find its positions: "))

positions = [index for index, value in enumerate(random_integers) if value == num]

if positions:
    print(f"The number {num} appears at positions: {positions}")
else:
    print(f"The number {num} does not appear in the list.")