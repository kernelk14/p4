"""
    SALARY COMPUTATION
"""
from grossSalary import GrossSalary, Employee
from SalaryDeductions import SalaryDeduction
from NetSalary import NetPay
# Here we need to input stuffs
names = input("Enter the name of the employee: ")
hrs = int(input("Enter the hours of work: "))
loans = int(input("Enter the loan amount: "))
insure = int(input("Enter your health insurance: "))

# We're setting things up here.
Employee.setName(names)
Employee.setHours(hrs)
Employee.setLoan(loans)
Employee.setInsurance(insure)

salary = GrossSalary.compute(hrs)
Employee.setSalary(salary)
print("-"*40)
print(f"Name: {Employee.getName()}")
print(f"Hours of work: {Employee.getHours()} hours")
print(f"Loan: {Employee.getLoan()} pesos")
print(f"Health Insurance: {Employee.getInsurance()} pesos")

print(f"Salary: {Employee.getSalary()} pesos")

deducted_salary = SalaryDeduction.deduct(Employee.getLoan())
Employee.setSalary(deducted_salary)

deducted_salary = SalaryDeduction.deduct(Employee.getInsurance())
Employee.setSalary(deducted_salary)
print(f"Salary after deducting your loan and health insurance: {int(Employee.getSalary())} pesos")

total_salary = NetPay.total()

print(f"Salary after deducting 12% tax : {int(total_salary)} pesos")
