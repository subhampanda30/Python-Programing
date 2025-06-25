#Program for Demonstrating Default Agruments
#DefaultArgsEx1.py
def dispstudinfo(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t{}\t\t{}\t{}".format(sno,sname,marks,crs))

#main program
print("="*50)
print("\tSNO\tName\tMarks\tCourse")
print("="*50)
dispstudinfo(10,"RS",34.56)# Function call
dispstudinfo(20,"JG",14.56)# Function call
dispstudinfo(30,"DR",44.66)# Function call
dispstudinfo(40,"KV",11.56)# Function call
print("="*50)
