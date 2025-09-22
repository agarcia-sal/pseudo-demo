def calculate_remainder_using_division(dividend, divisor):
    # Calculate quotient and remainder of the division
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # If there is a remainder, modify the return value based on the quotient
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return dividend  # If there is no remainder, return the dividend

def main():
    # Read input values for quantityA, quantityB, and size
    quantityA = int(input())
    quantityB = int(input())
    size = int(input())
    
    # Calculate results using the division function
    resultA = calculate_remainder_using_division(quantityA, size)
    resultB = calculate_remainder_using_division(quantityB, size)
    
    # Calculate the final result by multiplying the two results
    finalResult = resultA * resultB
    
    # Print the final result
    print(finalResult)

# Call the main function to execute the program
main()
