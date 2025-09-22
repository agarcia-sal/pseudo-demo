def calculate_remainder_and_adjustment(number, divisor):
    # Calculate quotient and remainder using integer division and modulus
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if the remainder is greater than 0
    if remainder > 0:
        # Return adjusted value based on the quotient and remainder
        return remainder * (quotient + 1)
    else:
        # If remainder is 0, return the original number
        return number

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Call the function for both n and m using s as the divisor
result_a = calculate_remainder_and_adjustment(n, s)
result_b = calculate_remainder_and_adjustment(m, s)

# Calculate the final result by multiplying the two results
final_result = result_a * result_b

# Print the final result
print(final_result)
