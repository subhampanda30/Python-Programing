#program for accepting Two numerical values and find big
#BigTwoEx1.py
a=float(input("Enter Value of a:"))
b=float(input("Enter Value of b:"))
#logic of finding Big
bv= a if a>b else b
print("big({},{})={}".format(a,b,bv))
