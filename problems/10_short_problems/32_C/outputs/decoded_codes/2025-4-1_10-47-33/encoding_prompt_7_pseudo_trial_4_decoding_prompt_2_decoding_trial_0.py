def calculate_remainder_and_product():
    def mc(number, divisor):
        quotient = number // divisor  # Calculate the integer quotient
        remainder = number % divisor   # Calculate the remainder
        
        if remainder > 0:
            return remainder * (quotient + 1)  # Return modified value based on remainder
        else:
            return number  # Return number if remainder is zero

    n = int(input())  # Read integer n
    m = int(input())  # Read integer m
    s = int(input())  # Read integer s

    resultA = mc(n, s)  # Calculate modified n using mc
    resultB = mc(m, s)  # Calculate modified m using mc

    print(resultA * resultB)  # Output the product of results

# Call the main function to execute
calculate_remainder_and_product()
