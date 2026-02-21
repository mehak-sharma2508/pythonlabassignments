# Steel Grading Program

# Input values
hardness = float(input("Enter Hardness: "))
carbon = float(input("Enter Carbon content: "))
tensile_strength = float(input("Enter Tensile Strength: "))

# Check conditions
cond1 = hardness > 50
cond2 = carbon < 0.7
cond3 = tensile_strength > 5600

# Determine grade
if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5

# Output
print(f"The grade of the steel is: {grade}")