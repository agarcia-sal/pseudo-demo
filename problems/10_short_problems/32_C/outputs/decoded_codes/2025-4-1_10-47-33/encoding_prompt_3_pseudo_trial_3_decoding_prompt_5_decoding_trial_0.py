def main():
    # Read input values for total1, total2, and divisor
    total1 = int(input())
    total2 = int(input())
    divisor = int(input())

    # Calculate and output the product of the adjusted values
    result = calculate_product_of_adjusted_values(total1, divisor) * calculate_product_of_adjusted_values(total2, divisor)
    print(result)

def calculate_product_of_adjusted_values(total, divisor):
    # Calculate quotient and remainder
    quotient = total // divisor
    remainder = total % divisor
    
    # Adjust value based on remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Entry point of the program
main()
