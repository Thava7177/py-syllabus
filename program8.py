f=open("samplep.txt","w")
for i in range(1,11):
    f.write("This is line %d\n"%i)
f.close()
f=open("samplep.txt","r")
f1=f.readlines()
print(f1)
for x in f1:
    print(x)
f.close()
