#PureKeyWordVarLenArgsEx1.py
def disp(**kvr): # Here **kvr is calle Keyword var length param and whose type dict
    print("----------------------------------")
    for k, v in kvr.items():
        print("\t{}--->{}".format(k, v))
    print()
    print("----------------------------------")
    # main program


disp(eno=10, ename="RS", sal=3.4, cname="TCS")  # Function call-1 with 4 Keyword args
disp(sno=100, sname="Mohan", hb1="Sleep", hb2="eating", hb3="chating")  # Function call-2 with 5 Keyword args
disp(tno=1000, tname="KVR", sub="PYTHON")  # Function call-3 with 3 Keyword args
