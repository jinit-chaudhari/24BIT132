food_items = [("Burger", 80), ("Pizza", 250), ("Pasta", 150), ("Sandwich", 60), ("Fries", 50)]

sorted_food_items = sorted(food_items, key=lambda item: item[1], reverse=True)

print("Food items sorted by price (high to low):")
for food, price in sorted_food_items:
    print(f"{food}: ₹{price}")
