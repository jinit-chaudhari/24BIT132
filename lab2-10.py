l =  int(input("enter a length"))
b =  int(input("enter a breadth"))

area = l * b
perimiter = 2*(l + b)

print("area",area)
print("perimiter",perimiter)


if(area > perimiter):
          print("the area is greater then perimiter")
else:
          print("the area is less then perimiter")
