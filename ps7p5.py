total_discount_given = 0.0  # Initialize the total discount accumulator

# Initial prompt
continue_program = input("Do you want to do this program (Yes/No)? ").strip().lower()

while continue_program == "yes":
    # Prompt for quantity and price of the item
    quantity = float(input("Enter quantity of the item: "))
    price = float(input("Enter price of the item: "))

    # Calculate extended price
    extended_price = quantity * price

    # Determine discount rate based on extended price
    discount_rate = 0.25 if extended_price > 10000.0 else 0.1
    # Calculate discount amount and total price after discount
    discount_amount = extended_price * discount_rate
    total_price_after_discount = extended_price - discount_amount

    # Update the total discount given
    total_discount_given += discount_amount

    # Display order details
    print(f"Extended price: ${extended_price:.2f}")
    print(f"Discount amount: ${discount_amount:.2f}")
    print(f"Total (after discount): ${total_price_after_discount:.2f}")

    # Prompt to continue
    continue_program = input("Do you want to process another order (Yes/No)? ").strip().lower()

# After exiting the loop, display the total discount given
print(f"Total discount given across all orders: ${total_discount_given:.2f}")



