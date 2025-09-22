def calculate_remainder_and_adjust(total, divisor):
    # Calculate quotient and remainder of total divided by divisor
    quotient = total // divisor
    remainder = total % divisor
    
    # If there is a remainder, adjust the output; otherwise, return the total
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Read input values for totalA, totalB, and divisor
total_a = int(input())
total_b = int(input())
divisor = int(input())

# Calculate the adjusted values for totalA and totalB using divisor
adjusted_value_a = calculate_remainder_and_adjust(total_a, divisor)
adjusted_value_b = calculate_remainder_and_adjust(total_b, divisor)

# Calculate the final result by multiplying the two adjusted values
final_result = adjusted_value_a * adjusted_value_b

# Output the final result
print(final_result)
