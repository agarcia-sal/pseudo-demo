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

    # Calculate modified values using mc
    resultA = mc(n, s)
    resultB = mc(m, s)

    # Output the product of resultA and resultB
    print(resultA * resultB)

# Call the main function to execute
calculate_remainder_and_product()
