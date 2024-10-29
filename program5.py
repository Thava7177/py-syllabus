def input_num():
    a=float(input("Enter a first Number :"))
    b=float(input("Enter a second Number :"))
    return(a,b)
x,y=input_num()
while True:
    if y==0:
        print("sorry cannot be divided by 0 please try again....!")
        x,y=input_num()
    else:
        print(x,"/",y," is ",x/y)
        break
