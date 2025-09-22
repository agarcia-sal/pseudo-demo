def adjust_quantity(total_count, step_size):
    """Adjusts the total count according to the step size."""
    quotient, remainder = divmod(total_count, step_size)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_count

# Read input values from the user
first_value = int(input())
second_value = int(input())
step_size = int(input())

# Calculate adjusted values
adjusted_first_value = adjust_quantity(first_value, step_size)
adjusted_second_value = adjust_quantity(second_value, step_size)

# Calculate and output the final product
final_product = adjusted_first_value * adjusted_second_value
print(final_product)
