#program for reading Two Numerical values from KBD and find the product
#MulEx2.py
x=float(input("Enter First value:"))
y=float(input("Enter Second Value:"))
z=x*y
print("Product({},{})={}".format(x,y,z))
print("==============OR================")
print("Product(%0.2f,%0.2f)=%0.2f" %(x,y,z))
print("==============OR================")
print("Product({},{})={}".format(x,y,round(z,2)))
