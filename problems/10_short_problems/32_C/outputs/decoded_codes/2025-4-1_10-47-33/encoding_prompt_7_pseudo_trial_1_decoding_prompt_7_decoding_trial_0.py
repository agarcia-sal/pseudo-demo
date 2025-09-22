def calculate_remainder_using_division(dividend, divisor):
    # Calculate quotient and remainder using integer division and modulus
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Check if there is a remainder
    if remainder > 0:
        # If remainder exists, return adjusted remainder
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original dividend
        return dividend

def main():
    # Read input values
    quantityA = int(input())
    quantityB = int(input())
    size = int(input())
    
    # Calculate results for both quantities
    resultA = calculate_remainder_using_division(quantityA, size)
    resultB = calculate_remainder_using_division(quantityB, size)
    
    # Calculate the final result by multiplying the two calculated results
    finalResult = resultA * resultB
    
    # Print the final result
    print(finalResult)

# Execute the main function
main()
