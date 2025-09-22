def calculate_modified_value(total, divisor):
    """
    Calculate the modified value based on the division of total by divisor.
    
    Args:
    total (int): The total value to be modified.
    divisor (int): The divisor value used for division.
    
    Returns:
    int: The modified value based on the remainder.
    """
    quotient = total // divisor    # Whole number result of division
    remainder = total % divisor     # Remainder after division
    
    if remainder > 0:
        return remainder * (quotient + 1)  # Modify value if remainder exists
    else:
        return total                     # Return original total if no remainder

# Main program
if __name__ == "__main__":
    # Read three integer values from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate modified values
    modified_n = calculate_modified_value(n, s)
    modified_m = calculate_modified_value(m, s)
    
    # Calculate the final result as the product of modified_n and modified_m
    final_result = modified_n * modified_m
    
    # Print the final result
    print(final_result)
