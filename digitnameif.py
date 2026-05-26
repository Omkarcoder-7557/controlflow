#WRITE A PYTHON PROGRAM WHICH WILL ACCEPT A DIGIT AND DISPLAY ITS NAME (if)
d=int(input("enter the digit "))

#logic
if (d==0):
    print("the {} is zero".format(d))
if (d==1):
    print("the {} is one".format(d))
if (d==2):
    print("the {} is two".format(d))
if (d==3):
    print("the {} is three".format(d))
if (d==4):
    print("the {} is four".format(d))
if (d==5):
    print("the {} is five".format(d))
if (d==6):
    print("the {} is six".format(d))
if (d==7):
    print("the {} is seven".format(d))
if (d==8):
    print("the {} is eight".format(d))
if (d==9):
    print("the {} is nine".format(d))
if d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("the {} is negative{}".format(d,d))
if d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] and d<0:
    print("the {} is negative number".format(d))
else:
    print("{} is a positive number not a digit".format(d))
print("the program executed")