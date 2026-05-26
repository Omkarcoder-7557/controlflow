#WRITE A PYTHON PROGRAM WHICH WILL ACCEPT A DIGIT AND DISPLAY ITS NAME
# (BY USING DICT AND IF ELSE OPERATOR)
dict={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",-1:"-one",-2:"-two",-3:"-three",-4:"-four",-5:"-five",-6:"-six",-7:"-seven",-8:"-eight",-9:"-nine"}
n=int(input("enter the number:"))
rel=" a positive number" if dict.get(n)==None and n>0 else "a negative number" if dict.get(n)==None and n<0 else dict.get(n)
print("the digit is {}".format(rel))