# Lab Assignment 2
# Copy python script without comments

source_file = input("Enter source python file name: ")
destination_file = input("Enter destination file name: ")

try:
    with open(source_file, 'r') as f1:
        lines = f1.readlines()

    new_lines = []

    for line in lines:
        stripped_line = line.strip()

        # Skip full line comments
        if not stripped_line.startswith("#"):
            # Remove inline comments
            if "#" in line:
                line = line.split("#")[0] + "\n"
            new_lines.append(line)

    with open(destination_file, 'w') as f2:
        f2.writelines(new_lines)

    print("\nOriginal File Content:")
    with open(source_file, 'r') as f1:
        print(f1.read())

    print("\nNew File Content (Without Comments):")
    with open(destination_file, 'r') as f2:
        print(f2.read())

except FileNotFoundError:
    print("File not found. Please check the file name.")