def search(string1 , string2):
    if string2 in string1:
        print("second string is in the first string")
    elif string1 in string2:
        print("first string is in the second string")
    else:
        print("second string is not in the first string & first string is not in the second string")

string1 = input("Enter the first string :")
string2 = input("Enter the second string :")
search(string1 , string2)