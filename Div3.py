#Program accepting Two Numbers from KBD and find Div
#This Program generates User-Friendly Error Message and It is Robust
#Div3.py
try:
    print("program Execution Started...")
    s1=input("Enter First Value:")
    s2=input("Enter Second value:")
    #convent S1 and s2 into int type
    a=int(s1)#----Exception generated statement-->ValueError
    b=int(s2)#----Exception generated statement-->ValueError
    c=a/b#---Exception generated statement-->Zero Division Error
except ZeroDivisionError:
    print("Don't Enter Zero For Den...")
    print("Enter Zero For Den...")
    print("Don't Enter alnums,strs and symbols")
else:
    print("----------")
    print("Div=",c)
    print("--------------")
finally:
    print("***********************************")
    print("Program Execution Ended....")
    print("************************************")



