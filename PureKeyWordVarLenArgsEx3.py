#PureKeyWordVarLenArgsEx3.py
def findtotal(sno,sname,cls,*vals,city="HYD",**submarks):
    print("-----------------------------------")
    print("Variable Length Vals")
    for val in vals:
        print("\t{}".format(val))
    print("-----------------------------------")
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    print("Student Class:{}".format(cls))
    print("Student Living City:{}".format(city))
    print("-----------------------------------")
    print("\tSubject Name\tSubject marks")
    print("-----------------------------------")
    totmarks=0
    for sub,marks in submarks.items():
        print("\t{}\t\t{}".format(sub,marks))
        totmarks=totmarks+marks
    print("-----------------------------------")
    print("TOTAL MARKS={}".format(totmarks))

#main program
findtotal(10,"RS","X",1,2,3,4,5,Eng=60,Hindi=50,Maths=88,Science=66,Social=77)
findtotal(20,"TR","XII",10,20,30,Maths=75,Physics=60,Chemistry=60)
findtotal(30,"MC","B.Tech(CSE)",1.2,2.3,4.5,5.5,OS=10,DBMS=11,Java=8,HTML=2,city="USA")
findtotal(40,"GV","Research",100,200,city="NL")

