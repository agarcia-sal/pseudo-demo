def calculate_remainder_adjusted_value(total, divisor):
    # Divide total by divisor to get quotient and remainder
    quotient = total // divisor
    remainder = total % divisor
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return total as is
        return total

# Read three numbers from the input
total1 = int(input())
total2 = int(input())
divisor = int(input())

# Calculate the adjusted values for total1 and total2 using the divisor
adjusted_value1 = calculate_remainder_adjusted_value(total1, divisor)
adjusted_value2 = calculate_remainder_adjusted_value(total2, divisor)

# Calculate and print the product of the two adjusted values
product = adjusted_value1 * adjusted_value2
print(product)
