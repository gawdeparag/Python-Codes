a=0
b=1
n=int(input("enter any number"))
print(a)
print(b)
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    print(c)

