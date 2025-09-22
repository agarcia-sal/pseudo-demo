def calculate_adjusted_values(n, m, s):
    # Calculate quotient and remainder for n
    quotient1 = n // s
    remainder1 = n % s
    
    # Adjust value for n based on the remainder
    if remainder1 > 0:
        adjusted_value1 = remainder1 * (quotient1 + 1)
    else:
        adjusted_value1 = n
    
    # Calculate quotient and remainder for m
    quotient2 = m // s
    remainder2 = m % s
    
    # Adjust value for m based on the remainder
    if remainder2 > 0:
        adjusted_value2 = remainder2 * (quotient2 + 1)
    else:
        adjusted_value2 = m
    
    # Return the product of the adjusted values
    return adjusted_value1 * adjusted_value2

# Read input values from the user
input_values = input().split()
n = int(input_values[0])
m = int(input_values[1])
s = int(input_values[2])

# Call the function and print the result
result = calculate_adjusted_values(n, m, s)
print(result)
