# Define a function to calculate remainder and product
def calculate_remainder_and_product():
    # Define a helper function to calculate modified value according to the rules
    def mc(number, divisor):
        # Calculate quotient and remainder
        quotient = number // divisor
        remainder = number % divisor
        
        # Check the remainder and return the appropriate value
        if remainder > 0:
            return remainder * (quotient + 1)
        else:
            return number

    # Read integers n, m, and s from input
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate modified results using mc
    result_a = mc(n, s)  # Calculate modified n
    result_b = mc(m, s)  # Calculate modified m

    # Calculate and print the product of resultA and resultB
    final_result = result_a * result_b
    print(final_result)

# Call the function to execute the logic
calculate_remainder_and_product()
