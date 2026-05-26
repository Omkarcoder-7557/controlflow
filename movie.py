#program for simple if statment
tiket=input("do you have movie ticket?(yes/no):").lower()
if tiket=="yes":
    print("go inside the theotor")
    print("watch the move")
    print("eat popcorn")
if tiket not in ["yes","no"]:
    print("learn typing first")
print("go to home ")