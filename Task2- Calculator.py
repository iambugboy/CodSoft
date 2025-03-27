def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("Select numb:  " "1.add  "  "2.sub  "  "3.mul  "  "4.divide")
sel=int(input("select task between 1 to 4: "))
n1=int(input("enter numb1: "))
n2=int(input("enter numb2: "))

if sel==1:
    print(n1,"+",n2,"=",add(n1,n2))
elif sel==2:
    print(n1,"-",n2,"=",sub(n1,n2))
elif sel==3:
    print(n1,"x",n2,"=",mul(n1,n2))
elif sel==4:
    print(n1,"/",n2,"=",div(n1,n2))
else:
    print("task number not enetered")
