#fileOpenEx1.py
try:
    fp=open("stdu1.data")
except FileNotFoundError:
    print("File does not Exist")
else:
    print("file opened in Read Mode Sucessfully")
    print("Type of fp=",type(fp))
    print("file Name:",fp.name)
    print("file Mode:",fp.mode)
    print("is file readable=",fp.readable())
    print("is file writable=",fp.writable())
    print("is file closed=",fp.closed)
finally:
    print("i am from finally block")
    fp.close()
    print("is file closed=",fp.closed)



