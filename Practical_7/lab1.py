print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")

ch = int(input("Enter your choice (1-5): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if ch == 1:
    print("Result:", a + b)

elif ch == 2:
    print("Result:", a - b)

elif ch == 3:
    print("Result:", a * b)

elif ch == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division not allowed")

elif ch == 5:
    print("Result:", a % b)

else:
    print("Invalid Choice")