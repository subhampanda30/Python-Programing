#program for accepting Two numerical values and find big
#BigTwoEx2.py
a=float(input("Enter Value of a:"))# 10
b=float(input("Enter Value of b:")) # 10
res=a if a>b else b if b>a else " Both values are equal"
print("big({},{})={}".format(a,b,res))