#Program accepting Two Numbers from KBD and find Div
#This Program generates User-Friendly Error Message and it is Robust
#Div2.py
try:
    print("Program Execution Strated...")
    s1=input("Enter First Value:")
    s2=input("Enter Second Value:")
    #Convert s1 and s2 into int type
    a=int(s1)#---Exception generated statement-->Value Error
    b=int(s2)#---Exception generated statement--->Value Error
    c=a/b#---Exception generated Statement --->Zero Division Error
    print("Don't Enter Zero For Den...")
except ValueError:
    print("Don't Enter alnums,strs and symbols")
else:
    print("--------------------------")
    print("Div=", c)
    print("--------------------------")
finally:
    print("******************************")
    print("Program Execution Ended...")
    print("******************************")
