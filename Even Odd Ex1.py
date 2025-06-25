#program for accepting a number and decding whether the given number is even or odd
#EvenOddEx1.py
n=int(input("Enter any number:"))
if(n%2==0):
    print("{} is Even".format(n))
if(n%2!=0):
    print("{} is Odd".format(n))