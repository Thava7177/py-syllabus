def gcd(x,y):
    if x>y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x%i==0)and(y%i==0):
            g=i
    return g
a=int(input("Enter a Number :"))
b=int(input("Enter a  another Number :"))
print("GCD of given two Number is :",gcd(a,b))
