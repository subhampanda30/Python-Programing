#This Program will not execute as it is
#Bcoz PVM Remembers Latest Function Fucntion Definition
#VarArgsEx1.py
def disp(a,b,c,d,e): #Function Def-1
    print(a,b,c,d,e)
def disp(a,b,c,d): #Function Def-2
    print(a, b, c, d)


def disp(a, b, c):  # Function Def-3
    print(a, b, c)


def disp(a, b):  # Function Def-4
    print(a, b)


def disp(a):  # Function Def-5
    print(a)

    # main program


disp(10, 20, 30, 40, 50)  # Function call-1 with 5 Args
disp(10, 20, 30, 40)  # Function call-2 with 4 args
disp(10, 20, 30)  # Function call-3 with 3 args
disp(10, 20)  # Function call-4 with 2 args
disp(10)  # Function call-5 with 1 args
