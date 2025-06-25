#Program for Demonstrating Default Agruments
#DefaultArgsEx4.py
def dispstudinfo1(sno,sname,marks,crs="PYTHON",cnt="USA"):
    print("\t{}\t{}\t\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

def dispstudinfo2(sno,sname,marks,crs="JAVA",cnt="INDIA"):
    print("\t{}\t{}\t\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))

#main program
print("="*50)
print("\tSNO\tName\tMarks\tCourse\tCountry")
print("="*50)

dispstudinfo1(20,"JG",14.56)# Function call
dispstudinfo1(60,"PT",31.56)# Function call
dispstudinfo1(70,"JB",66.66)
dispstudinfo1(80,"TR",33.33)
dispstudinfo1(10,"RS",34.56)# Function call
dispstudinfo1(55,"MC",24.56,cnt="INDIA")# Function call
print("="*50)
print("\tSNO\tName\tMarks\tCourse\tCountry")
print("="*50)
dispstudinfo2(30,"DR",44.66)# Function call
dispstudinfo2(40,"KV",11.56)# Function call
dispstudinfo2(50,"DT",21.56)# Function call
dispstudinfo2(65,"WS",14.56,cnt="USA")# Function call
print("="*50)

