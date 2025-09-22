def calculate_remainder_adjustment(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # Adjust the number if there's a remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

def main():
    # Read three integers from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Adjust n and m using the remainder adjustment function
    adjusted_n = calculate_remainder_adjustment(n, s)
    adjusted_m = calculate_remainder_adjustment(m, s)
    
    # Print the product of the adjusted values
    print(adjusted_n * adjusted_m)

# Call the main function to execute the program
main()
