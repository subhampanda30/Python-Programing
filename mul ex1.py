#program for reading Two Numerical values from KBD and find the product
#MulEx1.py
a=input("Enter First value:")
b=input("Enter Second Value:")
#c=a*b--TypeError
x=float(a)
y=float(b)
z=x*y
print("Product({},{})={}".format(x,y,z))
print("==============OR================")
print("Product(%0.2f,%0.2f)=%0.2f" %(x,y,z))
print("==============OR================")
k=round(z,2)
print("Product({},{})={}".format(x,y,k))

