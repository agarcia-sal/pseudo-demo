def calculate_remainder_and_product(n, m, s):
    def mc(number, divisor):
        quotient, remainder = divmod(number, divisor)  # Get quotient and remainder
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number
    
    n = int(input())  # Read integer n from input
    m = int(input())  # Read integer m from input
    s = int(input())  # Read integer s from input
    
    resultA = mc(n, s)  # Calculate modified n using mc
    resultB = mc(m, s)  # Calculate modified m using mc
    
    print(resultA * resultB)  # Output the product of resultA and resultB

# The function can be called as follows:
# calculate_remainder_and_product()  # Uncomment to execute
