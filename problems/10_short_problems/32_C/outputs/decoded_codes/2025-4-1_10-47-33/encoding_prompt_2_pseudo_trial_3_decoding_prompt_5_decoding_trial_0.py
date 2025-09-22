def mc(number, divisor):
    # Calculate the quotient and remainder of number divided by divisor
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if the remainder is greater than 0
    if remainder > 0:
        # Return the product of the remainder and the incremented quotient
        return remainder * (quotient + 1)
    else:
        # Return the original number if remainder is not greater than 0
        return number

# Read input values and convert them to integers
total1 = int(input())
total2 = int(input())
divisor = int(input())

# Process the inputs using the mc function
result1 = mc(total1, divisor)
result2 = mc(total2, divisor)

# Calculate and print the final product of the two results
final_product = result1 * result2
print(final_product)
