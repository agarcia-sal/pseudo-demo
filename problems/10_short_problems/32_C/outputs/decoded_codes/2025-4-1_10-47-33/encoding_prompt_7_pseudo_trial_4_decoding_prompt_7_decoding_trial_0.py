def calculate_remainder_and_product():
    # Helper function to calculate modified number based on divisor
    def mc(number, divisor):
        quotient = number // divisor  # Get the quotient of the division
        remainder = number % divisor   # Get the remainder of the division
        
        # If there is a remainder, calculate modified result
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number  # If no remainder, return the original number
    
    # Read integers n, m, and s from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate modified values using the mc function
    resultA = mc(n, s)  # Calculate modified n
    resultB = mc(m, s)  # Calculate modified m
    
    # Output the product of resultA and resultB
    print(resultA * resultB)  # Print the final result

# To run the function
calculate_remainder_and_product()
