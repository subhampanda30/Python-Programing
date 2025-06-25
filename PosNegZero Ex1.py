#Program for accepting a numerical Integer values and decide whether it is +ve or -ve or zero
#PosNegZeroEx1.py
n=float(input("Enter a Number:")) # +ve   -120   or 0
if(n>0):
    print("{} is +VE".format(n))
if(n<0):
    print("{} is -VE".format(n))
if(n==0):
    print("{} is ZERO".format(n))
print("Program execution Completed")