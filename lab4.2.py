def to_lower(str):
    result = ""
    for char in str:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_upper(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle_case(string):
    result = ""
    for char in string:
        if 'a' <= char <= 'z':
            # Convert to uppercase
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            # Convert to lowercase
            result += chr(ord(char) + 32)
        else:
            result += char
    return result


string = input("Enter a string: ")
print("Lower Case:", to_lower(string))
print("Upper Case:", to_upper(string))
print("Toggle Case:", toggle_case(string))