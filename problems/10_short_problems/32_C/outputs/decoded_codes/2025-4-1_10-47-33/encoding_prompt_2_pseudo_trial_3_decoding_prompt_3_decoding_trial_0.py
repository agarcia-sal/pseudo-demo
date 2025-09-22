def mc(number, divisor):
    # Calculate the quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if there is a remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Input Section
total1, total2, divisor = map(int, input().split())

# Processing Section
result1 = mc(total1, divisor)
result2 = mc(total2, divisor)

# Output Section
final_product = result1 * result2
print(final_product)
