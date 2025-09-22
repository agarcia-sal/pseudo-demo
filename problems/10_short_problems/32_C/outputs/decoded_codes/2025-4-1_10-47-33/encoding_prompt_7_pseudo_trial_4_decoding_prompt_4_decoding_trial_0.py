def calculate_remainder_and_product():
    def mc(number, divisor):
        quotient = number // divisor
        remainder = number % divisor
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number

    # Read integers n, m, and s from input
    n = int(input())
    m = int(input())
    s = int(input())

    resultA = mc(n, s)  # Calculate modified n using mc
    resultB = mc(m, s)  # Calculate modified m using mc

    # Output the product of resultA and resultB
    print(resultA * resultB)

# Call the main function
calculate_remainder_and_product()


        10
        20
        3
        

        60
        

        15
        25
        5
        

        75
        

        0
        0
        1
        

        0
        