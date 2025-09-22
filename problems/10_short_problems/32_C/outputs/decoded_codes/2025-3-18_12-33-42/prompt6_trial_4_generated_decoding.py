def calculate_remainder(number, divisor):
    # Perform integer division to get quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # If there's a remainder, return the modified value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number  # If no remainder, return the original number

# Read inputs from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate the modified remainders for both n and m
modified_n = calculate_remainder(n, s)
modified_m = calculate_remainder(m, s)

# Calculate the final result by multiplying the modified values
result = modified_n * modified_m

# Output the result
print(result)
