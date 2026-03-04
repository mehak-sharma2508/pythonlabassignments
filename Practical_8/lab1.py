# Lab Assignment 1
# Read a file and write its content in uppercase to another file

source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

try:
    with open(source_file, 'r') as f1:
        content = f1.read()

    upper_content = content.upper()

    with open(destination_file, 'w') as f2:
        f2.write(upper_content)

    print("\nContent successfully copied in uppercase!")

    print("\nOriginal File Content:")
    print(content)

    print("\nNew File Content (Uppercase):")
    print(upper_content)

except FileNotFoundError:
    print("File not found. Please check the file name.")