numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

print("Total number of items:", len(numbers))

if len(numbers) > 0:
    print("Last item:", numbers[-1])
else:
    print("Tuple is empty")

print("Tuple in reverse order:", numbers[::-1])

if 5 in numbers:
    print("Yes")
else:
    print("No")

if len(numbers) > 2:
    new_tuple = tuple(sorted(numbers[1:-1]))
    print("After removing first and last, sorted tuple:", new_tuple)
else:
    print("Not enough elements to remove first and last")