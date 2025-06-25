#Program fort swapping of any two values
#AssigmentOperatorEx1.py
a=input("Enter Value of a:")
b=input("Enter Value of b:")
print("="*50)
print("Original Val of a:{}".format(a))
print("Original Val of b:{}".format(b))
#swapping Logic using Multi Line assigment operator
a,b=b,a
print("="*50)
print("Swapped Val of a:{}".format(a))
print("Swapped Val of b:{}".format(b))
print("="*50)