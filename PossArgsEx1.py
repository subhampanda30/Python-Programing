#Proghram for Demonstarting Positional Args
#PossArgsEx1.py
def dispstudinfo(sno,sname,marks):
    print("\t{}\t{}\t\t{}".format(sno,sname,marks))

#main program
print("="*50)
print("\tSNO\tName\tMarks")
print("="*50)
dispstudinfo(10,"RS",34.56)# Function call
dispstudinfo(20,"JG",14.56)# Function call
dispstudinfo(30,"DR",44.66)# Function call
dispstudinfo(40,"KV",11.56)# Function call
print("="*50)
