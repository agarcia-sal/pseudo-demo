def mc(number, divisor):
    """Calculate a specific value based on the division of `number` by `divisor`."""
    quotient = number // divisor
    remainder = number % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number


def main():
    # Read three integers from input
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate the two results using the mc function
    result1 = mc(n, s)
    result2 = mc(m, s)
    
    # Print the product of the two results
    print(result1 * result2)


if __name__ == "__main__":
    main()
