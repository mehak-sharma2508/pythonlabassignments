# Diamond Pattern (Without Spaces Center)

rows = 5

# Upper Part
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Lower Part
for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()