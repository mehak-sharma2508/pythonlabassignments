# PRACTICAL 3
# TASK 1..

print("Pattern 1")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


print("\nPattern 2")
for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()


print("\nPattern 3")
for i in range(1, 6):
    for j in range(i, 0, -1):
        print(j, end="")
    print()


print("\nPattern 4")
for i in range(1, 6):
    num = 1
    for j in range(1, i + 1):
        print(num, end=" ")
        num=1-num
    print()


print("\nPattern 5")
num = 2
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()


print("\nPattern 6")
for i in range(1, 6):
    print("*" * i)