def b_s(a,key):
    start=0
    end=len(a)
    while(start<end):
        mid=(start+end)//2
        if a[mid]>key:
            end=mid
        elif a[mid]==key:
            return mid    
        else:
            start=mid+1           
    return -1
a=[]
n=int(input("Enter a Number of item in list :"))
for i in range(n):
    item=int(input())
    a.append(item)
print(a)
a=[int(x) for x in a]
key=int(input("enter your target value :"))
b=b_s(a,key)
if b<0:
    print("sorry element ",key," is not found in a list " )
else:
    print("Found a element ",key,"index position is ",b)
