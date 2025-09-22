def calculate_remainder_and_total(n, s):
    # Divide n by s to get the quotient and remainder
    quotient = n // s
    remainder = n % s

    # If remainder is greater than zero, calculate adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

def main():
    # Read three integers from input: n, m, and s
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate the adjusted values for n and m using s
    adjusted_value_n = calculate_remainder_and_total(n, s)
    adjusted_value_m = calculate_remainder_and_total(m, s)

    # Calculate and print the product of the adjusted values
    print(adjusted_value_n * adjusted_value_m)

# Execute the main function
if __name__ == "__main__":
    main()
