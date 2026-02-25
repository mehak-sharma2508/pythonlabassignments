balance = 1000

def display_balance():
    print("Current Balance:", balance)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    balance += amount
    print("Amount Deposited Successfully")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print("Amount Withdrawn Successfully")
    else:
        print("Insufficient Balance")

print("1. Display Current Balance")
print("2. Deposit Amount")
print("3. Withdraw Amount")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    display_balance()
elif choice == 2:
    deposit()
elif choice == 3:
    withdraw()
else:
    print("Invalid Choice")