# Define a function to adjust the quantity based on the step size
def adjust_quantity(total_count, step_size):
    # Calculate the quotient and remainder when dividing total_count by step_size
    quotient = total_count // step_size
    remainder = total_count % step_size
    
    # Adjust the quantity based on the remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_count

# Read input values from the user and convert them to integers
first_value = int(input())
second_value = int(input())
step_size = int(input())

# Calculate the adjusted values using the adjust_quantity function
adjusted_first_value = adjust_quantity(first_value, step_size)
adjusted_second_value = adjust_quantity(second_value, step_size)

# Calculate the final product of the adjusted values
final_product = adjusted_first_value * adjusted_second_value

# Output the result
print(final_product)
