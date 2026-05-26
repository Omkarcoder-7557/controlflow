#program for the finding the biggest among three value
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
#logic
if b<=a>c:
    print("big({},{},{})={}".format(a,b,c,a))
elif c<=b>a:
    print("big({},{},{})={}".format(a,b,c,b))
elif a<=c>b:
    print("big({},{},{})={}".format(a,b,c,c))
elif(a==b==c):
    print("all three value are same")
print("the program executed successfully")