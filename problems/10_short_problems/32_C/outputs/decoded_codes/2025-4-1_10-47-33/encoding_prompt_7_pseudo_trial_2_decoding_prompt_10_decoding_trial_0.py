def calculate_remainder_adjustment(number, divisor):
    """Calculate the adjusted value based on the remainder."""
    quotient = number // divisor
    remainder = number % divisor
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number


def main():
    """Main function to read inputs and calculate the product of adjusted values."""
    n = int(input())
    m = int(input())
    s = int(input())
    
    adjusted_n = calculate_remainder_adjustment(n, s)
    adjusted_m = calculate_remainder_adjustment(m, s)
    
    print(adjusted_n * adjusted_m)


if __name__ == "__main__":
    main()
