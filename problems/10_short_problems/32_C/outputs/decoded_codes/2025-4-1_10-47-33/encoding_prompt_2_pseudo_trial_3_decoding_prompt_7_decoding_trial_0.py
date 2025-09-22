# Start Program

def mc(number, divisor):
    # Calculate the quotient (q) and remainder (r) of dividing number by divisor
    q = number // divisor  # Integer division to get the quotient
    r = number % divisor   # Modulo operation to get the remainder
    
    # If remainder (r) is greater than 0
    if r > 0:
        # Return product of remainder (r) and incremented quotient (q + 1)
        return r * (q + 1)
    else:
        # Otherwise, return the original number
        return number

# Input Section
# Read input from the user and convert them to integers
total1 = int(input())
total2 = int(input())
divisor = int(input())

# Processing Section
# Call the mc function with total1 and divisor, store the result in result1
result1 = mc(total1, divisor)
# Call the mc function with total2 and divisor, store the result in result2
result2 = mc(total2, divisor)

# Output Section
# Calculate the final product of result1 and result2
final_product = result1 * result2
# Print the final product
print(final_product)

# End Program
