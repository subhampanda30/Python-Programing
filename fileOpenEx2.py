#fileOpenEx2.py
fp=open("stud.data","w")
print("File Created and Opened in write Mode")
print("Type of fp=",type(fp))
print("is file closed befoer close()=",fp.closed)
fp.close()
print("is file after close()=",fp.closed)
