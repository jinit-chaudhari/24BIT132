import math
n=int(input("enter n number here:"))
r=int(input("enter r number here:"))
a=math.factorial(n)
b=math.factorial(r)
c=math.factorial(n-r)
ncr=(a)/b*c
print("ncr","=",ncr)
npr=a/c
print("npr","=",npr)