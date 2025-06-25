#Program for Demonstarting Keyword Arguments
#KwdArgsEx1.py
def   disp(a,b,c,d):
    print("\t{}\t{}\t{}\t{}".format(a,b,c,d))

print("="*50)
print("\tA\tB\tC\tD")
print("="*50)
disp(10,20,30,40)
disp(d=40,c=30,b=20,a=10)
disp(c=30,d=40,a=10,b=20)
disp(10,20,d=40,c=30)
#disp(c=30,d=40,10,20) SyntaxError: positional argument follows keyword argument

print("="*50)
