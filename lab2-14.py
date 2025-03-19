a=int(input("enter the mark of math"))
b=int(input("enter the mark of phy"))
c=int(input("enter the mark of computer"))

avg =( a + b + c ) / 3
total = a + b + c

print("avg is = " , avg )
print("total mark is = " , total)

if(a<39 or b<39 or c<39):
    print("your fail your grade is F")
elif(40 <= a <= 44 or 40 <= b <= 44 or 40 <= c <= 44 ):
    print("your grade is P")
elif(45<=a<=49 or 45<=b<=49 or 45<=c<=49):
    print("your grade is c")
elif(50<=a<=54 or 50<=b<=54 or 50<=c<=54):
    print("your grade is b")
elif(55<=a<=59 or 55<=b<=59 or 55<=c<=59):
    print("your grade is B+")
elif(60<=a<=69 or 60<=b<=69 or 60<=c<=69):
    print("your grade is A")
elif(70<=a<=79 or 70<=b<=79 or 70<=c<=79):
    print("your grade is A+")
elif(80<=a<=100 or 80<=b<=100 or 80<=c<=100 ):
    print("your grade is O")
