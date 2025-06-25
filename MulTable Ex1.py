#program for generating Mul table for a given number
#MulTableEx1.py
n=int(input("Enter a Number for generating Mul table:"))
if(n<=0):
    print("{} is Invalid input".format(n))
else:
    print("=" * 50)
    print("Mul Table for :{}".format(n))
    print("="*50)
    i=1 # Initlization part
    while(i<=10): # Cond Part
        print("\t{} x {} = {}".format(n,i,n*i))
        i=i+1 #Updation Part
    else:
        print("="*50)