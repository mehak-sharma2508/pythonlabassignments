# Proper Centered Pyramid

rows = 5

for i in range(rows):

    # Left side spaces (double space for proper centering)
    print("  " * (rows - i - 1), end="")

    # Print stars (1,3,5,7,9)
    for j in range(2 * i + 1):
        print("* ", end="")

    print()