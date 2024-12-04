"""
    SALARY COMPUTATION
"""
from grossSalary import GrossSalary

"""
    John, 200 hrs, 500php,  
"""

fileAppend = open("salaries.txt", 'w')

name = input("Enter the name of the employee: ")
hrs = int(input("Enter the hours of work: "))
loan = int(input("Enter the loan amount: "))
insure = int(input("Enter your health insurance: "))

salary = GrossSalary.compute(hrs)

fileAppend.write(f"\"{name}\",{hrs},{salary},{loan},{insure}")
fileAppend.write("\n")
fileAppend.close()

fileRead = open("salaries.txt", 'r')
salaries = fileRead.readlines()
for sal in salaries:
    print(sal)

fileRead.close()

