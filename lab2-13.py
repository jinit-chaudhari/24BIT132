
def number_to_words(n):
    words = [
        "zero", "one", "two", "three", "four", "five", 
        "six", "seven", "eight", "nine", "ten", 
        "eleven", "twelve", "thirteen", "fourteen", 
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
 

for i in range(20):
    print(f"{i} → {number_to_words(i)}")
