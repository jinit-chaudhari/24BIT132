def remove_substring(main_str, remove_str):
    m, n = len(main_str), len(remove_str)
    result = ""
    i = 0

    while i < m:
        if main_str[i:i+n] == remove_str:
            i += n
        else:
            result += main_str[i]
            i += 1
    return result


main_string = input("Enter the main string: ")
remove_string = input("Enter the string to remove: ")

print("Final String:", remove_substring(main_string, remove_string))
