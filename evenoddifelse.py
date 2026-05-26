#WRITE A PYTHON PROGRAM WHICH WILL ACCEPT NO AND CHEK
# IT IS EVEN OR ODD (ONLY FOR +VE NUMBER)(if else)
n=int(input("enter a number:"))
if n<0:
    print("this is negative number bro")
else:
    if n%2==0:
        print("even number")
    else:
        if n%2!=0:
          print("odd number")
print("the program execution is finished")