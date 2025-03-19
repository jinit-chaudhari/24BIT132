def count_boys_and_girls(names_list):
    boys_count = sum(1 for name in names_list if isinstance(name, tuple))
    girls_count = sum(1 for name in names_list if isinstance(name, str))
    
    return boys_count, girls_count

names = [("Viraj",), "Dhruvi", ("Meet",), "Bhakti", "Kavya", ("Ujas",), "Nidhi"]

boys, girls = count_boys_and_girls(names)

print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")