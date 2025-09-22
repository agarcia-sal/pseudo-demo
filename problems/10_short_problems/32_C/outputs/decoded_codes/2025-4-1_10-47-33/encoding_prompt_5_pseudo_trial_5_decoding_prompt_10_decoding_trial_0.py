def calculate_remainder_and_adjust(total, divisor):
    """
    Calculate the adjusted output based on the total and divisor.
    
    If there is a remainder when dividing total by divisor,
    returns remainder multiplied by (quotient + 1).
    Otherwise, returns total.

    Args:
        total (int): The total value to adjust.
        divisor (int): The divisor used for the calculations.

    Returns:
        int: The adjusted value.
    """
    # Calculate quotient and remainder
    quotient, remainder = divmod(total, divisor)
    
    # Adjust output based on remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total


# Read input values
totalA = int(input())
totalB = int(input())
divisor = int(input())

# Calculate adjusted values for totalA and totalB
adjusted_value_A = calculate_remainder_and_adjust(totalA, divisor)
adjusted_value_B = calculate_remainder_and_adjust(totalB, divisor)

# Calculate the final result by multiplying the two adjusted values
final_result = adjusted_value_A * adjusted_value_B

# Output the final result
print(final_result)
