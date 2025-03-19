prices = {
    "apple": 60,
    "banana": 30,
    "milk": 60,
    "tomato": 40,
    "coffee": 5
}
quantity = {
    "apple": 2,
    "banana": 5,
    "milk": 1,
    "tomato": 2,
    "coffee": 12
}
total_bill = 0

for item in quantity:
    if item in prices:
        total_bill += prices[item] * quantity[item]

print("Total Bill Amount: ₹", total_bill)