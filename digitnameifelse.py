#WRITE A PYTHON PROGRAM WHICH WILL ACCEPT A DIGIT AND DISPLAY ITS NAME (if else)
d=int(input("enter the digit:"))

#logic
if (d==0):
    print("the {} is zero".format(d))
else:
    if (d==1):
        print("the {} is one".format(d))
    else:
        if (d==2):
            print("the {} is two".format(d))
        else:
            if (d==3):
                print("the {} is three".format(d))
            else:
                if (d == 4):
                    print("the {} is four".format(d))
                else:
                    if (d == 5):
                        print("the {} is five".format(d))
                    else:
                        if (d == 6):
                            print("the {} is six".format(d))
                        else:
                            if (d == 7):
                                print("the {} is seven".format(d))
                            else:
                                if (d == 8):
                                    print("the {} is eight".format(d))
                                else:
                                    if (d == 9):
                                        print("the {} is nine".format(d))
                                    else:
                                        if d in [-1, -2, -3, -4, -5, -6, -7, -8, -9]:
                                            print("the {} is negative{}".format(d,d))
                                        else:
                                            if d not in [-1, -2, -3, -4, -5, -6, -7, -8, -9] and d < 0:
                                                print("the {} is negative number not a digit".format(d))
                                            else:
                                                if d not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] and d > 0:
                                                    print("the {} is positive number not a digit".format(d))
print("the program executed")