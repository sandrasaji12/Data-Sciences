num=int(input("enter the limit"))
n1,n2 = 0 , 1
print("fibonacci series:")
print(n1)
print(n2)
print(end="")
for i in range(2,num):
    n3 = n1 + n2
    n1=n2
    n2=n3
    print(n3,end="")
    print()
