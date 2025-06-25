#program for Finding Product  of First N Natural Numbers
#NatNumsProductEx1.py
n=int(input("Enter How Many Natural Nums Product u want:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("-" * 50)
    print("Product of First {} Natural Numbers ".format(n))
    print("-" * 50)
    p=1 # Multiplucative Identity
    d=1
    while(d<=n):
        print("\t{}".format(d))
        p=p*d
        d=d+1
    else:
        print("-"*50)
        print("Prouct={}".format(p))
        print("-" * 50)