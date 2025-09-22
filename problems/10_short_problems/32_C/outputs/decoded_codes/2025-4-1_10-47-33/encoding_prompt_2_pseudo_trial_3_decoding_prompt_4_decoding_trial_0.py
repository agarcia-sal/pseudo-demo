def mc(number, divisor):
    # Calculate the quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # If remainder is greater than zero, return adjusted product
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Input section: read three integers
total1 = int(input())
total2 = int(input())
divisor = int(input())

# Processing section: call mc function
result1 = mc(total1, divisor)
result2 = mc(total2, divisor)

# Output section: calculate and print the final product
final_product = result1 * result2
print(final_product)
