
x = int(input("enter X coordinate of cricle for the center"))
y = int(input("enter Y coordinate of cricle for the center"))
x1 = int(input("enter X1 coordinate of cricle for any point on the circle"))
y1 = int(input("enter Y1 coordinate of cricle for any point on the circle"))
r = int(input("enter radious of the circle"))
distance = ( pow(x - x1 , 2 ) + pow(y - y1 , 2 ) )
distance1 = pow(distance,1/2)
print(r)
print(distance1)

if(distance1 > r):
    print("point is out side of circle")
elif(distance1 < r):
    print("point is in side of circle")
elif(distance1 == r):
    print("point is on the circle")
