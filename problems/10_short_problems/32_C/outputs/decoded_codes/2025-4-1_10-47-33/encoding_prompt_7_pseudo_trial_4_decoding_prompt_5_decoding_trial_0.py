def calculate_remainder_and_product():
    def mc(number, divisor):
        # Calculate quotient and remainder
        quotient, remainder = divmod(number, divisor)
        # Check if remainder is greater than 0
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number

    # Read integers n, m, and s from input
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate modified n and m using mc
    result_a = mc(n, s)
    result_b = mc(m, s)

    # Output the product of resultA and resultB
    print(result_a * result_b)

# To run the function, uncomment the line below
# calculate_remainder_and_product()
