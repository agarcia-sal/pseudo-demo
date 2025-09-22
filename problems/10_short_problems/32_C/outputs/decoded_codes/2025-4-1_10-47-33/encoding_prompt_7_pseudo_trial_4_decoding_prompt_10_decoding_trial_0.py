def calculate_remainder_and_product():
    def mc(number, divisor):
        # Perform integer division to get quotient and remainder
        quotient = number // divisor
        remainder = number % divisor
        
        # Determine the return value based on the remainder
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number

    # Read three integers from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate modified values using mc function
    resultA = mc(n, s)  # Calculate modified n
    resultB = mc(m, s)  # Calculate modified m
    
    # Output the product of the results
    print(resultA * resultB)

# Example of calling the function
calculate_remainder_and_product()
