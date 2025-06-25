#This Program will  execute as it is
#PureVarArgsEx3.py
def disp(*kvr):# here * kvr is called Variable length Parameter and type is called tuple
    for val in kvr:
        print("{}".format(val),end="  ")
    print()

#main program
disp(10,20,30,40,50) # Function call-1 with 5 Args
disp(10,20,30,40) # Function call-2 with 4 args
disp(10,20,30) # Function call-3 with 3 args
disp(10,20) # Function call-4 with 2 args
disp(10) # Function call-5 with 1 args
disp() # Function call-6 with 0 args"""
