def calculate_remainder_and_product():
    def mc(number, divisor):
        # Divide number by divisor to get quotient and remainder
        quotient = number // divisor
        remainder = number % divisor
        
        # Check if the remainder is greater than 0
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number
    
    # Read integers n, m, and s from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate modified values using mc
    resultA = mc(n, s)  # Calculate modified n
    resultB = mc(m, s)  # Calculate modified m
    
    # Output the product of resultA and resultB
    print(resultA * resultB)

# Call the function to execute
calculate_remainder_and_product()
