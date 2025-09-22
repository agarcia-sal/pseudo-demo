def adjust_quantity(total_count, step_size):
    """
    Adjusts the total count based on how it divides by the step size.
    
    Parameters:
        total_count (int): The total quantity to evaluate.
        step_size (int): The value which divides the total count.

    Returns:
        int: Adjusted quantity based on the divisibility condition.
    """
    quotient, remainder = divmod(total_count, step_size)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_count

def main():
    """
    Main function to read inputs and calculate the product of adjusted quantities.
    """
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

# Entry point of the program
if __name__ == "__main__":
    main()
