def calculate_remainder_using_division(dividend, divisor):
    # Calculate the quotient and remainder of the division
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Check if there is a remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend

def main():
    # Read input values for quantityA, quantityB, and size
    quantityA = int(input())
    quantityB = int(input())
    size = int(input())
    
    # Calculate remainder using division for both quantities
    resultA = calculate_remainder_using_division(quantityA, size)
    resultB = calculate_remainder_using_division(quantityB, size)
    
    # Calculate the final result as the product of resultA and resultB
    final_result = resultA * resultB
    
    # Print the final result
    print(final_result)

# Call the main function to execute the program
main()
