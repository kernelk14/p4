""" Source code of NetSalary.py """

# Basically SalaryDeduction deducts the expenses for you, 
# so NetSalary will only deduct the tax (12% of your gross salary.)

from grossSalary import Employee, GrossSalary
from SalaryDeductions import SalaryDeduction

class NetPay:
    def total():
        taxDeduct = SalaryDeduction.deduct(float(Employee.getSalary()) * 0.12)
        return taxDeduct
