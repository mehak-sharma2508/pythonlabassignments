# Short Vendor Annual Purchase Report

# Vendor details
name = input("Vendor Name: ")
year = input("Year of Association: ")
contact = input("Contact Number: ")
email = input("Email ID: ")

# Monthly purchases input
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
purchases = [float(input(f"{m}: ")) for m in months]

# Annual report
total = sum(purchases)
avg = total / 12

print(f"\nVendor: {name}, Year: {year}")
print(f"Total Purchase: Rs. {total}, Average Monthly: Rs. {avg:.2f}")
print("Monthly Purchases:")
for m, p in zip(months, purchases):
    print(f"{m}: Rs. {p}")
