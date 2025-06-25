#This Program will  execute as it is
#Bcoz PVM Remembers Latest Function Fucntion Definition
#VarArgsEx2.py
def disp(a,b,c,d,e): #Function Def-1
    print(a,b,c,d,e)
disp(10,20,30,40,50) # Function call-1 with 5 Args
#----------------------------------------------------
def disp(a,b,c,d): #Function Def-2
    print(a,b,c,d)
disp(10,20,30,40) # Function call-2 with 4 args
#----------------------------------------------------
def disp(a,b,c): #Function Def-3
    print(a, b, c)


disp(10, 20, 30)  # Function call-3 with 3 args


# ----------------------------------------------------
def disp(a, b):  # Function Def-4
    print(a, b)


disp(10, 20)  # Function call-4 with 2 args


# ----------------------------------------------------
def disp(a):  # Function Def-5
    print(a)


disp(10)  # Function call-5 with 1 args
