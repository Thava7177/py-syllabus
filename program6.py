class employee:
    def persnol(self):
        print("\t\t\tEMPLOYEE DETAILS...")
        name=input("Enter Employee Name :")
        no=input("Enter Employee Number :")
        print("Employee Name :",name)
        print("Employee Number :",no)
class salary(employee):
    def netsal(self):
        bs=int(input("Enter Your Basic Salary :"))
        ta=int(input("Enter your TA :"))
        hra=int(input("Enter Your HRA :"))
        pf=int(input("Enter Your PF :"))
        net=(bs+ta+hra)-pf
        print("Your NetSalary is :",net)
class leave(salary):
    def lop(self):
        l=int(input("Enter your Last Month Leave :"))
        if l<10:
            print("no LOP..")
        else:
            print("Avoid leave Taken ..Lost of pay....")
o=leave()
n=int(input("enter a number of employye we want..."))
for i in range(n):
    o.persnol()
    o.netsal()
    o.lop()
