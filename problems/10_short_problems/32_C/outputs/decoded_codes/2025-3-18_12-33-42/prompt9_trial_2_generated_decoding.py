def calculate_remainder_product(total_items, divisor):
    # Calculate the quotient and remainder using integer division
    quotient, remainder = divmod(total_items, divisor)
    
    # If there's a remainder, compute the specific product
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Main Program
input_line = input()  # Read input line
total_items_1, total_items_2, divisor = map(int, input_line.split())  # Split and convert to integers

# Calculate products using the defined function
product_1 = calculate_remainder_product(total_items_1, divisor)
product_2 = calculate_remainder_product(total_items_2, divisor)

# Calculate final output
final_result = product_1 * product_2

# Display result
print(final_result)
