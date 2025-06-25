#PureKeyWordVarLenArgsEx2.py
def findtotal(sno,sname,cls,**submarks):
    print("-----------------------------------")
    print("Student Number:{}".format(sno))
    print("Student Name:{}".format(sname))
    print("Student Class:{}".format(cls))
    if(len(submarks)!=0):
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
findtotal(10,"RS","X",Eng=60,Hindi=50,Maths=88,Science=66,Social=77)
findtotal(20,"TR","XII",Maths=75,Physics=60,Chemistry=60)
findtotal(30,"MC","B.Tech(CSE)",OS=10,DBMS=11,Java=8,HTML=2)
findtotal(40,"GV","Research")

