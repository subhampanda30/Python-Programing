#Program for Demonstarting Positional Args
#PossArgsEx2.py
def dispstudinfo(sno,sname,marks,crs):
    print("\t{}\t{}\t\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("="*50)
print("\tSNO\tName\tMarks\tCourse")
print("="*50)
dispstudinfo(10,"RS",34.56,"PYTHON")# Function call
dispstudinfo(20,"JG",14.56,"PYTHON")# Function call
dispstudinfo(30,"DR",44.66,"PYTHON")# Function call
dispstudinfo(40,"KV",11.56,"PYTHON")# Function call
print("="*50)
