#Shares.py--File Name and Module Name
def Sharesinfo():
    d={"IT":51,"JKTYRE":51,"AUTO":12,"HL":11,"FIN":350}
    return d
import shares,time,importlib
def dispshares(d):
    print("----------------------------------")
    print("Share Name\tShareValue")
    print("----------------------------------")
    for sn,sv in d.items():
        print("\t{}\t\t{}".format(sn,sv))
    else:
        print("----------------------------------")
#main program
d=shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 15 seconds")
time.sleep(15)
print("I am Coming-out off sleep after 15 seconds")
importlib.reload(shares)
d=shares.sharesinfo()
dispshares(d)
print("I am going to sleep for 15 seconds")
time.sleep(15)
print("I am Coming-out off sleep after 15 seconds")
importlib.reload(shares)
d=shares.sharesinfo()
dispshares(d)


