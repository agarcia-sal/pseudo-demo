def adjust_quantity(total_count, step_size):
    """
    Adjusts the provided total count based on its divisibility by the step size.
    
    Parameters:
    total_count (int): The total quantity to be adjusted.
    step_size (int): The step size that dictates the adjustment logic.
    
    Returns:
    int: The adjusted quantity based on the specified conditions.
    """
    quotient = total_count // step_size
    remainder = total_count % step_size
    
    if remainder > 0:
        return (quotient + 1) * remainder
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
