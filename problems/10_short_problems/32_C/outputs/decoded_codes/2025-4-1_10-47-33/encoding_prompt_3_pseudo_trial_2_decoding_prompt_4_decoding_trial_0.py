def calculate_remainder_count_and_multiply(input_value, divisor):
    # Calculate the quotient and remainder
    quotient = input_value // divisor
    remainder = input_value % divisor
    
    # If there is a remainder, return the product of the remainder and the next quotient value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return input_value  # Return the original input if there's no remainder

# Start Main Program
# Read three integer inputs from user
input_value1 = int(input())
input_value2 = int(input())
divisor = int(input())

# Calculate the results for input_value1 and input_value2 using the defined function
result1 = calculate_remainder_count_and_multiply(input_value1, divisor)
result2 = calculate_remainder_count_and_multiply(input_value2, divisor)

# Multiply the results and output the final result
final_result = result1 * result2
print(final_result)
