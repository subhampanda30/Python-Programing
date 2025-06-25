#Program for Demonstrating Default Agruments
#DefaultArgsEx2.py
def dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t{}\t\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("="*50)
print("\tSNO\tName\tMarks\tCourse\tCountry")
print("="*50)
dispstudinfo(10,"RS",34.56)# Function call
dispstudinfo(20,"JG",14.56)# Function call
dispstudinfo(30,"DR",44.66)# Function call
dispstudinfo(40,"KV",11.56)# Function call
print("="*50)
