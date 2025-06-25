#SimpleInt.py
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate:"))
#cal si
si=(p*t*r)/100
#cal totamt
totamt=p+si
print("="*50)
print("\tSimple Interest Result")
print("="*50)
print("\tPrinciple Amount:{}".format(p))
print("\tTime:{}".format(t))
print("\tRate of Interest:{}".format(r))
print("-"*50)
print("\tSimple Interest:{}".format(si))
print("\tTOTAL AMOUNT TO PAY:{}".format(totamt))
print("="*50)