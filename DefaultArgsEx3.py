#Program for Demonstrating Default Agruments
#DefaultArgsEx3.py
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
dispstudinfo(50,"DT",21.56,"JAVA","USA")# Function call
dispstudinfo(60,"PT",31.56,cnt="RSA")# Function call
dispstudinfo(70,"JB",66.66,cnt="USA",crs="HTML")
print("="*50)
