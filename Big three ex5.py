#BigThreeEx1.py
a=int(input("Enter Value of a:"))
b=int(input("Enter Value of b:"))
c=int(input("Enter Value of c:"))
#Code for finding a big
if(a>=b) and (a>c):
    print("big({},{},{})={}".format(a,b,c,a))
#Code for finding b big
if(b>a) and (b>=c):
    print("big({},{},{})={}".format(a,b,c,b))
#Code for finding c big
if(c>=a) and (c>b):
    print("big({},{},{})={}".format(a, b, c, c))
if(a==b) and (b==c):
    print("all values are equal")