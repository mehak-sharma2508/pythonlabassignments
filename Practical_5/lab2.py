prices = tuple(map(float, input("Enter prices separated by space: ").split()))

print("Total items sold:", len(prices))

if len(prices) > 0:
    print("Cheapest item sold:", min(prices))

    costliest = max(prices)
    print("Costliest item sold:", costliest)

    print("Price list  in ascending order:", tuple(sorted(prices)))

    print("Number of costliest items sold:", prices.count(costliest))
else:
    print("No items sold")