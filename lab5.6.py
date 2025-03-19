def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

fahrenheit_temp = [32, 50, 68, 77, 100]

celsius_temp = [fahrenheit_to_celsius(f) for f in fahrenheit_temp]

print("Fahrenheit temperatures:", fahrenheit_temp)
print("Equivalent Celsius temperatures:", celsius_temp)