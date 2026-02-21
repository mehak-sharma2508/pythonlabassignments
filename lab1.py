# Program to store employee details and calculate salary.

# Input employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

# Allowances
DA = 0.92 * basic_salary
HRA = 0.58 * basic_salary
TA = 0.30 * basic_salary

# Deduction
LIC = 500

# Salary Calculation
gross_salary = basic_salary + DA + HRA + TA
net_salary = gross_salary - LIC

# Display details
print("\n----- Employee Details -----")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)

print("\n----- Salary Details -----")
print("Basic Salary:", basic_salary)
print("DA (92%):", DA)
print("HRA (58%):", HRA)
print("TA (30%):", TA)
print("LIC Deduction:", LIC)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)