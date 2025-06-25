
#Function for addition of Two Numbers
#Approach4.py
def sumop():
    x= float(input("Enter First value:"))
    y= float(input("Enter Second value:"))
    z=x+y
    return x,y,z # Here return statement can return One or More Number of values

#main program
k,v,res=sumop() # Function call with Multi Line assignment
print("Sum({},{})={}".format(k,v,res))
print("--------------OR--------------------")
res=sumop() # Function call with Single Line Assigment
#here res is of type <class,'tuple'>
print("Sum({},{})={}".format(res[0],res[1],res[2]))
print("Sum({},{})={}".format(res[-3],res[-2],res[-1]))
