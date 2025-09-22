def calculate_remainder_adjustment(number, divisor):
    # Perform integer division and calculate the remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if the remainder is greater than 0
    if remainder > 0:
        # Return the adjusted value
        return remainder * (quotient + 1)
    else:
        # Return the original number if no adjustment is needed
        return number

def main():
    # Read three integers from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate adjusted values for n and m
    adjusted_n = calculate_remainder_adjustment(n, s)
    adjusted_m = calculate_remainder_adjustment(m, s)
    
    # Print the product of adjusted values
    print(adjusted_n * adjusted_m)

# Call the main function to execute the program
main()
