#program for the finding the biggest among three value
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
#logic
if a>=b and a>c:
    print("big({},{},{})={}".format(a,b,c,a))
if b>a and b>=c:
    print("big({},{},{})={}".format(a,b,c,b))
if c>=a and c>b:
    print("big({},{},{})={}".format(a,b,c,c))
if(a==b==c):
    print("all three value are same")
print("the program executed successfully")