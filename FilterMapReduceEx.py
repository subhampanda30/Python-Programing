#FilterMapReduceEx.py

#write a Python Program which will accept list of salary with in the range of 0 to 1000.
#Get the Emp salary ranges from 0 to 500.and also get 501 to 1000 from the list of out salary.
#Give 10% Hike to all the Employee who salary rages from 0 to 500 and give 20% Hike for those Employee 501 to 1000.
#Find the total salary of those Employee ranges from whoes salary 0 to 500 and also find total salary of those Employee whose salary ranges from 501 to 1000.

import functools
print("Enter List of Salaries of Employees:")
sallist=[float (sal) for sal in input().split() if float (sal)>0 and float(sal)<=1000]
print("-------------")
print("Given Sal List=",sallist)
print("-------------")
#Filter the salaries range from 0 to 500
sal0_500=list(filter(lambda sal:0<=sal<=500,sallist))
#Filter the salaries range from 501 to 1000
sal501_1000=list(filter(lambda sal:501<=sal<1000,sallist))
#Give Hike 10% for those employee ranges from 0 to 500
hikesal0_500=list(map(lambda sal:sal+sal*10/100,sal0_500))
#Give Hike 20% for those employee ranges from 501 to 1000
hikesal501_1000=list(map(lambda sal:sal+sal*20/100,sal501_1000))
#Find total sal of 0 to 500
totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500)
#Find total sal of 0 to 500 after Hike
tothikesal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal0_500)
#Find total sal of 501 to 1000
totsal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,sal501_1000)
#Find total sal of 501 to 1000 After Hike
tothikesal501_1000=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal501_1000)
print("======================================")
print("Old Sal0-500\tHikeSal0-500")
print("======================================")
for osal,nsal in zip(sal0_500,hikesal0_500):
    print("\t{}\t\t{}".format(osal,nsal))
print("---------------------------------------")
print("\t{}\t\t{}".format(totsal0_500,tothikesal0_500))
print("======================================")
print("Old Sal501-1000\tHikeSal501-1000")
print("======================================")
for osal,nsal in zip(sal501_1000,hikesal501_1000):
    print("\t{}\t\t{}".format(osal,nsal))
print("---------------------------------------")
print("\t{}\t\t{}".format(totsal501_1000,tothikesal501_1000))
print("======================================")
