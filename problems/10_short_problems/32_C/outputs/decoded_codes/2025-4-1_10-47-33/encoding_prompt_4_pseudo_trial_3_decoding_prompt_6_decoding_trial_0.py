# Define the mc function which calculates a specific value based on division
def mc(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # If remainder is greater than 0, calculate and return
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # Return the number if remainder is 0
        return number

# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
