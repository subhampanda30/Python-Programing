#PureVarArgsEx5.py
def disp(sno,sname,*vals,city="HYD"):# here * vals is called Variable length Parameter and type is called tuple
    print("--------------------------------")
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    print("Student Living City:{}".format(city))
    s=0
    for val in vals:
        print("{}".format(val),end="  ")
        s=s+val
    print()
    print("sum={}".format(s))
    print("--------------------------------")
#main program
disp(100,"Rossum",10,20,30,40,50) # Function call-1 with 5 Args
disp(200,"Travis",10,20,30,40) # Function call-2 with 4 args
disp(300,"Dennis",10,20,30) # Function call-3 with 3 args
disp(400,"KVR",10,20) # Function call-4 with 2 args
disp(500,"Kinney",10) # Function call-5 with 1 args
disp(600,"Naresh") # Function call-6 with 0 args
disp(700,"Dtrump",1.2,2.3,3.4,city="USA")
#disp(800,"Putin",city="RSA",11.2,22.3,33.4)--SyntaxError: positional argument follows keyword argument
