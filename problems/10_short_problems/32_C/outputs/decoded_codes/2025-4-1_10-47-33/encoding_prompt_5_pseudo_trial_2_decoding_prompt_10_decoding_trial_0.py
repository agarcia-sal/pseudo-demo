def calculate_adjusted_groups(value, group_size):
    """
    Divides a value into groups of specified size and adjusts based on remainder.
    
    Args:
        value (int): The number to be divided into groups.
        group_size (int): The size of each group.
        
    Returns:
        int: Adjusted value based on the division.
    """
    quotient = value // group_size
    remainder = value % group_size
    
    if remainder > 0:
        # If there's a remainder, include one extra group
        return remainder * (quotient + 1)
    else:
        # If no remainder, return the original value
        return value


def main():
    # Read input values for n, m, and s from the user
    n = int(input())
    m = int(input())
    s = int(input())
    
    # Calculate the adjusted group values for n and m
    adjusted_n = calculate_adjusted_groups(n, s)
    adjusted_m = calculate_adjusted_groups(m, s)

    # Calculate the product of the two adjusted values
    product = adjusted_n * adjusted_m

    # Output the result of the product
    print(product)


if __name__ == "__main__":
    main()
