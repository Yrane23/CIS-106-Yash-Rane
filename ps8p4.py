
with open('data2.txt', 'r') as file:
    lines = file.readlines()

total_extended_price = 0.0
order_count = 0
for i in range(0, len(lines), 3):
    item = lines[i].strip()
    quantity = int(lines[i + 1].strip())
    price = float(lines[i + 2].strip())
    extended_price = quantity * price
    total_extended_price += extended_price
    order_count += 1
    print(f"{item} {quantity} {price} {extended_price}")

average_order = total_extended_price / order_count if order_count else 0
print(f"Sum of all extended prices: ${total_extended_price}")
print(f"Count of the number of orders: {order_count}")
print(f"Average order: ${average_order}")
