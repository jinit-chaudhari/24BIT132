import random

odd_integers = [random.choice(range(1, 101, 2)) 
    for i in range(5)]
print("List of 5 odd integers:", odd_integers)


even_integers = [random.choice(range(2, 101, 2)) 
    for i in range(4)]
print("List of 4 even integers:", even_integers)


odd_integers[2] = even_integers
print("After replacing the third element of odd integers with the list of even integers:", odd_integers)
 
flattened_list = []
for item in odd_integers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)  

print("Flattened list:", flattened_list)


flattened_list.sort()
print("Sorted flattened list:", flattened_list)