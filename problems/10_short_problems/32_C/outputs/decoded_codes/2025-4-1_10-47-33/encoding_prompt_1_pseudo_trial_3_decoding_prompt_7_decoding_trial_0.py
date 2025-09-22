def calculate_remainder_and_adjustment(number, divisor):
    # Calculate quotient and remainder when number is divided by divisor
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if remainder is greater than 0
    if remainder > 0:
        # Adjust the return value based on the quotient and remainder
        return remainder * (quotient + 1)
    else:
        # If remainder is 0, return the original number
        return number

# Read input values for n, m, and s from standard input
n = int(input())
m = int(input())
s = int(input())

# Call the function for n and m using s as the divisor and store results
RESULT_A = calculate_remainder_and_adjustment(n, s)
RESULT_B = calculate_remainder_and_adjustment(m, s)

# Calculate the final result by multiplying both results 
FINAL_RESULT = RESULT_A * RESULT_B

# Print the final result
print(FINAL_RESULT)
