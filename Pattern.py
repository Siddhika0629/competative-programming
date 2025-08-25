'''n=int(input("enter a number:"))
for i in range(0,n):
    print("*",end="")'''


'''n=int(input("enter a number:"))
m=int(input("enter a number:"))
for i in range(0,n):
    for j in range(0,m):
        print("*",end="")
    print()'''


'''n=int(input("enter a number:"))
m=int(input("enter a number:"))
for i in range (0,n,n+1):
    for j in range(0,m,):
     print("*",end="")
print()'''


'''n=int(input("enter a number:"))
for i in range (1,n+1):
    for j in range(1,i+1):
        if(j%2==0):
            print("*",end="")
        else:
            print(j,end="")
    print()'''


n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==1 or j==n):
            print("*" ,end="")
        else:
            print("_",end="")
    print()