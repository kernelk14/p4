""" Source code of SalaryDeductions.py """

from grossSalary import Employee

class SalaryDeduction:
    def deduct(value):
        return Employee.getSalary() - value 
