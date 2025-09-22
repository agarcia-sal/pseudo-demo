def calculate_remainder_and_adjust(value, divisor):
    # Calculate the quotient and remainder when dividing value by divisor
    quotient = value // divisor
    remainder = value % divisor
    
    # Adjust the value based on the remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

def main():
    # Read three integers from input
    total_value1 = int(input())
    total_value2 = int(input())
    divisor = int(input())
    
    # Calculate adjusted values using the defined function
    adjusted_value1 = calculate_remainder_and_adjust(total_value1, divisor)
    adjusted_value2 = calculate_remainder_and_adjust(total_value2, divisor)
    
    # Calculate the product of the adjusted values
    product = adjusted_value1 * adjusted_value2
    
    # Print the result of the product
    print(product)

# Run the main function only if this is the main module
if __name__ == "__main__":
    main()
