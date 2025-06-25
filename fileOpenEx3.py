#fileOpenEx3.py
with open("stud1.data","w")as fp:
    print("File Created and Opened in write Mode")
    print("Type of fp=",type(fp))
    print("File Name:",fp.name)
    print("Fie Name:",fp.mode)
    print("is file Readable=",fp.readable())
    print("is fie writable=",fp.writable())
    print("is file Closed=",fp.closed)
print("-------------------------")
print("is file Closed=",fp.closed)
