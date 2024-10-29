import math
while True:
    print("1.factorial \n2.power \n3.area of circle \n4.squreroot \n5.exit")
    ch=int(input("Enter Your choise :"))
    if ch==1:
        a=int(input("Enter a number to find factorial :"))
        print("A given number factorial is :",math.factorial(a))
    elif ch==2:
        a=int(input("enter your base number :"))
        b=int(input("Enter Your power number :"))
        print(a,"power of ",b,"is",math.pow(a,b))
    elif ch==3:
        r=float(input("Enter readius of a circle :"))
        print("area of circle is ",math.pi*r*r)
    elif ch==4:
        a=float(input("Enter a number to find squreroot :"))
        print("squreroot of given Number is ",math.sqrt(a))
    elif ch==5:
        print(exit())
    else:
        print("Invalid Input.. try again..")
        
