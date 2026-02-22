# TASK 4

rows = 5

for i in range(rows):
    # left spaces increase
    for s in range(i):
        print(" ", end="")

    # stars decrease
    for j in range(rows - i):
        print("*", end=" ")

    print("\n")