# Define the function to calculate adjusted value based on a divisor
def adjusted_value(value, divisor):
    # Calculate quotient and remainder
    quotient = value // divisor  # Integer division for the quotient
    remainder = value % divisor   # Remainder from the division
    
    # Check if there is a remainder
    if remainder > 0:
        # Return the adjusted value based on the remainder
        return remainder * (quotient + 1)
    else:
        # Return the original value if perfectly divisible
        return value

# Read input values
n = int(input())  # Read n value as an integer
m = int(input())  # Read m value as an integer
s = int(input())  # Read s value as an integer

# Calculate the adjusted values using the defined function
first_adjusted_value = adjusted_value(n, s)
second_adjusted_value = adjusted_value(m, s)

# Calculate the product of the two adjusted values
product_of_adjusted_values = first_adjusted_value * second_adjusted_value

# Output the result
print(product_of_adjusted_values)
