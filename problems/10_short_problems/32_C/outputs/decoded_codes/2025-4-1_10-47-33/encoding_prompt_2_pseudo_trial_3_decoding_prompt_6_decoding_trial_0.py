# Define a function that calculates the modified quotient and remainder
def mc(number, divisor):
    # Calculate the quotient and remainder of dividing number by divisor
    quotient = number // divisor  # Integer division gives us the quotient
    remainder = number % divisor   # Modulus operation gives us the remainder

    # If the remainder is greater than 0, return specific product
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number  # If no remainder, return the original number

# Input section: Read three integers from input
total1 = int(input())
total2 = int(input())
divisor = int(input())

# Processing section: Call mc function for total1 and total2
result1 = mc(total1, divisor)
result2 = mc(total2, divisor)

# Output section: Calculate and print the final product of result1 and result2
final_product = result1 * result2
print(final_product)
