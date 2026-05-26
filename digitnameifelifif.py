#WRITE A PYTHON PROGRAM WHICH WILL ACCEPT A DIGIT AND DISPLAY ITS NAME (if else....if)
d=int(input("enter the digit:"))
#logic
if (d==0):
    print("the {} is zero".format(d))
elif (d==1):
    print("the {} is one".format(d))
elif (d==2):
    print("the {} is two".format(d))
elif (d==3):
    print("the {} is three".format(d))
elif (d==4):
    print("the {} is four".format(d))
elif (d==5):
    print("the {} is five".format(d))
elif (d==6):
    print("the {} is six".format(d))
elif (d==7):
    print("the {} is seven".format(d))
elif (d==8):
    print("the {} is eight".format(d))
elif (d==9):
    print("the {} is nine".format(d))
elif d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("the {} is negative{}".format(d,d))
elif d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9] and d<0:
    print("the {} is negative number not a digit".format(d))
elif d not in [0,1,2,3,4,5,6,7,8,9] and d>0:
    print("the {} is positive number not a digit".format(d))
print("the program executed")