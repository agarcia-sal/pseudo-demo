def adjusted_value(value, divisor):
    """Calculate the adjusted value based on the divisor."""
    quotient, remainder = divmod(value, divisor)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

def main():
    # Read input values from standard input
    n = int(input())
    m = int(input())
    s = int(input())

    # Calculate adjusted values for n and m
    first_adjusted_value = adjusted_value(n, s)
    second_adjusted_value = adjusted_value(m, s)

    # Output the product of the two adjusted values
    product = first_adjusted_value * second_adjusted_value
    print(product)

if __name__ == "__main__":
    main()
