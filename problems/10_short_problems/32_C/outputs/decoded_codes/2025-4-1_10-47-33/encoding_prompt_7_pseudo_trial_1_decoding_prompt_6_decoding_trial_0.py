def calculate_remainder_using_division(dividend, divisor):
    # Perform division to get quotient and remainder
    quotient = dividend // divisor  # Integer division to get quotient
    remainder = dividend % divisor    # Remainder of the division
    
    # Check if there is a remainder
    if remainder > 0:
        # Return modified remainder if there is a remainder
        return remainder * (quotient + 1)
    else:
        # Return the original dividend if there is no remainder
        return dividend

def main():
    # Read input values for quantityA, quantityB, and size
    quantity_a = int(input())
    quantity_b = int(input())
    size = int(input())
    
    # Calculate results using the provided quantities and size
    result_a = calculate_remainder_using_division(quantity_a, size)
    result_b = calculate_remainder_using_division(quantity_b, size)
    
    # Calculate the final result as the product of result_a and result_b
    final_result = result_a * result_b
    
    # Output the final result
    print(final_result)

# Call the main function to execute the program
main()
