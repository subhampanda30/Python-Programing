#MatchCaseEx2.py
import sys
s="""=======================================
			Area of Different Figures
=======================================
				C. Circle
				R. Rectangle
				S. Square
				T. Triangle
				E. Exit
======================================="""
print(s)
ch=input("Enter Ur Choice:")
match(ch):

    case "C"|'c':
        r=float(input("Enter Radius:"))
        ac=3.14*r**2
        print("Area of Circle:{}".format(ac))
    case "R"|'r':
        l,b=float(input("Enter Length:")),float(input("Enter Breadth:"))
        ar=l*b
        print("Area of Rect:{}".format(ar))
    case "S"|'s':
        side = float(input("Enter Side:"))
        sa = side**2
        print("Area of Sqaure:{}".format(sa))
    case 'T'|'t':
        b, h = float(input("Enter Base:")), float(input("Enter Height:"))
        at=0.5*b*h
        print("Area of Triangle:{}".format(at))
    case "E"|'e':
        print("Thx for using program ")
        sys.exit()
    case _:
        print("Ur Selection of Operation is wrong--try again")



