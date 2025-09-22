def adjust_quantity(total_count, step_size):
    # Calculate quotient and remainder using integer division and modulus
    quotient = total_count // step_size
    remainder = total_count % step_size
    
    # If there is a remainder, return the adjusted quantity
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_count

# Read input values from user
first_value = int(input())
second_value = int(input())
step_size = int(input())

# Calculate adjusted values using the adjust_quantity function
adjusted_first_value = adjust_quantity(first_value, step_size)
adjusted_second_value = adjust_quantity(second_value, step_size)

# Calculate and output the final product of the adjusted values
final_product = adjusted_first_value * adjusted_second_value
print(final_product)
