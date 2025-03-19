str = input("Enter a string: ")
char_freq = {}

for char in str:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1

print("Character Frequency Dictionary:")
print(char_freq)