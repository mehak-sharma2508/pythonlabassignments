# Ohm's Law Current Calculator

# Input voltage and resistance
V = float(input("Enter Voltage (V) in volts: "))
R = float(input("Enter Resistance (R) in ohms: "))

# Calculate current using Ohm's Law
I = V / R

# Display current
print(f"Current (I) = {I:.2f} A")

# Display nature of current
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")