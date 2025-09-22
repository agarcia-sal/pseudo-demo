def calculate_remainder_and_adjust(total, divisor):
    """
    This function calculates the adjusted value based on the total and divisor.
    It uses the division to determine the quotient and remainder, and adjusts
    the output accordingly.
    
    :param total: The total value to adjust.
    :param divisor: The divisor to use for calculation.
    :return: Adjusted value based on the remainder of the total divided by the divisor.
    """
    quotient = total // divisor  # Calculate integer division (quotient)
    remainder = total % divisor   # Calculate remainder

    # Adjust output based on the presence of a remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total


# Read input values
totalA = int(input())
totalB = int(input())
divisor = int(input())

# Calculate the adjusted values for totalA and totalB using the divisor
adjusted_value_a = calculate_remainder_and_adjust(totalA, divisor)
adjusted_value_b = calculate_remainder_and_adjust(totalB, divisor)

# Calculate the final result by multiplying the two adjusted values
final_result = adjusted_value_a * adjusted_value_b

# Output the final result
print(final_result)
