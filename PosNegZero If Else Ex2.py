#Program for accepting a numerical Integer values and decide whether it is +ve or -ve or zero
#PosNegZeroIfElseEx1.py
n=float(input("Enter a Number:")) # 120   -120   or 0
if(n>0):
    print("{} is +VE".format(n))
else:
    if(n<0):
        print("{} is -VE".format(n))
    else:
        print("{} is ZERO".format(n))
    print("Program execution Completed--inner if--else")
print("Program execution Completed--outer if--else")


