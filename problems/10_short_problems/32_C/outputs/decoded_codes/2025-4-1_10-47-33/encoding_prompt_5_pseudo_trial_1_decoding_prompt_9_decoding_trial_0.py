def adjust_quantity(total_count, step_size):
    # Calculate the quotient and remainder
    quotient = total_count // step_size
    remainder = total_count % step_size
    
    # Adjust the quantity based on the remainder
    if remainder > 0:
        # Return remainder multiplied by (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # If no remainder, return total_count
        return total_count

# Read input values from the user
first_value = int(input())
second_value = int(input())
step_size = int(input())

# Calculate adjusted values
adjusted_first_value = adjust_quantity(first_value, step_size)
adjusted_second_value = adjust_quantity(second_value, step_size)

# Calculate and output the final product
print(adjusted_first_value * adjusted_second_value)
