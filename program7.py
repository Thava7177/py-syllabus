class compute:
    def area(self,x=None,y=None,z=None):
        if(x!=None and y!=None and z!=None):
            return x+y+z
        elif(x!=None and y!=None):
            return x*y
        elif(x!=None):
            return 3.14*x*x
o=compute()
r=float(input("Enter your readius of circle :"))
print("Area of circle is :",o.area(r))
b=float(input("Enter Your Breath of Reactangle :"))
l=float(input("Enter Your length of Reactangle :"))
print("Area Of Reactangle is :",o.area(b,l))
s=float(input("Enter a side of triangle :"))
b=float(input("Enter a base of triangle :"))
os=float(input("Enter a another side of triangle :"))
print("Area Of triangle is :",o.area(b,s,os))
