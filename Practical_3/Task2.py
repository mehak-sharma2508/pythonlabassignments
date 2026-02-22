# PRACTICAL 3
# TASK 2

print("Pattern 1")
for i in range(1, 6):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()


print("\nPattern 2")
for i in range(1, 6):
    for j in range(1, i+1):
        if j % 2 == 1:
            print(".", end=" ")
        else:
            print("#", end=" ")
    print()


print("\nPattern 3")
letters = ['P','y','t','h','o']

for i in range(5):
    for j in range(i + 1):
        print(letters[i], end="")
    print()


print("\nPattern 4")

word = "python"

for i in range(1, len(word) + 1):
    for j in range(i):
        print(word[j], end=" ")
    print()