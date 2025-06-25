#Program accepting Two Numbers from KBD and find Div
#This is Program is weak Program bcoz It generates Technical Error Messages
#Div1.py
print("Program Execution Strated...")
s1=input("Enter First Value:")
s2=input("Enter Second Value:")
#Convert s1 and s2 into int type
a=int(s1)#----Exception generated Statement-->ValueError
b=int(s2)#----Exception generated Statement-->ValueError
c=a/b #----Exception generated Statement-->ZeroDivisionError
print("Div=",c)
print("Program Execution Ended...")
