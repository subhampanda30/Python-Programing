#SimpleInt.py
def simpleintcal():
    p=float(input("Enter Principle Amount:"))
    t=float(input("Enter Time:"))
    r=float(input("Enter Rate:"))
    if(p>=0) and (t>=0) and (r>=0):
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
    else:
        print("Invalid Input Entered--try again")

#main program
simpleintcal()
