#RectAreaPeri.py
def rectareaperi():
    #accept length and Breadth
    l=float(input("Enter Length:"))
    b=float(input("Enter Breadth:"))
    if(l>=0) and  (b>=0):
        ar=l*b
        pr=2*(l+b )
        return l,b,ar,pr
    else:
        return ("Invalid Input",)
#main program
result=rectareaperi() # Function call
if(len(result)>1):
    print("="*50)
    print("Length={}".format(result[0]))
    print("Breadth={}".format(result[1]))
    print("Area of Rect={}".format(result[2]))
    print("Perimeter of Rect={}".format(result[3]))
    print("="*50)
else:
    print("Invalid Length and Breadth")
