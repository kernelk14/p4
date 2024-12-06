""" Source code of grossSalary.py """

# How to compute for the gross salary?

# Gross salary is the salary of an employee before any deductions.

# Every hr = 500

# I will put the Employee class here.
class Employee:
    employeeTable = {}
        
    def setName(nm):
        Employee.employeeTable["name"] = nm
    def setHours(hr):
        Employee.employeeTable["hours"] = hr
    def setLoan(ln):
        Employee.employeeTable["loan"] = ln
    def setInsurance(ins):
        Employee.employeeTable["insurance"] = ins
    def setSalary(sal):
        Employee.employeeTable["salary"] = sal

    def getName():
        return Employee.employeeTable["name"]
    def getHours():
        return Employee.employeeTable["hours"]
    def getLoan():
        return Employee.employeeTable["loan"]
    def getInsurance():
        return Employee.employeeTable["insurance"]
    def getSalary():
        return Employee.employeeTable["salary"]



class GrossSalary:
    fixed_salary = 500
    def compute(hours):
        gs = hours * 500
        return gs

    
    
