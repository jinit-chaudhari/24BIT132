tup = (1, 2, 3, 4, 5, 6)
temp_list = list(tup)

temp_list.remove(3)
modified_tup = tuple(temp_list)
print("Modified Tuple :", modified_tup)