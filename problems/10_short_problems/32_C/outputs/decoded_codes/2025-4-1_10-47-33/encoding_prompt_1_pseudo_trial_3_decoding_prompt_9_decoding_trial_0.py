def calculate_remainder_and_adjustment(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # If remainder is greater than 0, return adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values from standard input
n = int(input())
m = int(input())
s = int(input())

# Call the function for n and m using s as the divisor
result_A = calculate_remainder_and_adjustment(n, s)
result_B = calculate_remainder_and_adjustment(m, s)

# Calculate the final result
final_result = result_A * result_B

# Print the final result
print(final_result)
