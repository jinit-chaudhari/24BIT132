x1 = int(input("enter a x coordinate of point 1 "))
y1 = int(input("enter a y coordinate of point 1 "))
x2 = int(input("enter a x coordinate of point 2 "))
y2 = int(input("enter a y coordinate of point 2 "))
x3 = int(input("enter a x coordinate of point 3 "))
y3 = int(input("enter a y coordinate of point 3 "))

m1 = (y3 - y2) /(x3 - x2)
m2 =(y2 - y1)/(x2 - x1)
m3 = (y3 - y1)/(x3 - x1)


print("slope 1",m1)
print("slope 2",m2)
print("slope 3",m3)

if( m1 == m2 == m3 ):
    print("points are in straight")
else:
    print("points are not in straight")    
