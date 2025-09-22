def calculate_remainder_adjustment(number, divisor):
    quotient, remainder = divmod(number, divisor)  # Divide and get quotient and remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjust if there's a remainder
    else:
        return number  # Return the original number if no remainder

def main():
    n, m, s = map(int, input().split())  # Read three integers
    adjusted_n = calculate_remainder_adjustment(n, s)  # Adjust n
    adjusted_m = calculate_remainder_adjustment(m, s)  # Adjust m
    print(adjusted_n * adjusted_m)  # Output the product of adjusted values

main()  # Call the main function
