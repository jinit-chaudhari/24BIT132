string = input("enter a string here:")
alpha = 0
digits = 0
for char in string:
    if char.isalpha():
       alpha = alpha+1
        
    elif char.isdigit():
        digits = digits+1
       
print("No. of alphabets :", alpha)
print("No. of digits :", digits)