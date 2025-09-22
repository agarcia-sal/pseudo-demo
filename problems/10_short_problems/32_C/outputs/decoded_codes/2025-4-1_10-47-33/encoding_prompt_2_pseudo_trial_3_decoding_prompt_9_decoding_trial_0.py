# Define a function that performs a calculation based on the number and the divisor
def mc(number, divisor):
    # Calculate the quotient and the remainder
    q = number // divisor  # Quotient
    r = number % divisor   # Remainder
    
    # Check if remainder is greater than 0
    if r > 0:
        # Return modified product
        return r * (q + 1)
    else:
        # Return the original number if remainder is 0
        return number

# Input Section
# Read three integers from user input
total1 = int(input())
total2 = int(input())
divisor = int(input())

# Processing Section
# Call the mc function with total1 and divisor
result1 = mc(total1, divisor)
# Call the mc function with total2 and divisor
result2 = mc(total2, divisor)

# Output Section
# Calculate the final product of result1 and result2
final_product = result1 * result2
# Print the final product
print(final_product)
