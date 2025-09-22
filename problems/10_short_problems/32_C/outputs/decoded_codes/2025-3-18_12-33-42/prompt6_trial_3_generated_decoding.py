def calculate_remainder_and_adjust(number, divisor):
    # Divide number by divisor and get both quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # If there is a remainder, adjust the result using the quotient
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read three integers from input
total1 = int(input())
total2 = int(input())
divisor = int(input())

# Calculate the adjusted values for total1 and total2
adjusted_total1 = calculate_remainder_and_adjust(total1, divisor)
adjusted_total2 = calculate_remainder_and_adjust(total2, divisor)

# Calculate and display the product of the two adjusted values
print(adjusted_total1 * adjusted_total2)
