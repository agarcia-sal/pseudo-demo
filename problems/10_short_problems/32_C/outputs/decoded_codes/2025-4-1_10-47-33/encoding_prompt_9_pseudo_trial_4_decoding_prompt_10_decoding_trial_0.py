def calculate_groups(total_items, group_size):
    """
    Calculate the effective number of items based on complete groups.
    
    Args:
    total_items (int): The total number of items to group.
    group_size (int): The size of each group.
    
    Returns:
    int: The effective number of items considering any remainder.
    """
    quotient = total_items // group_size
    remainder = total_items % group_size
    
    if remainder != 0:
        return remainder * (quotient + 1)
    else:
        return total_items


def main():
    # Input three integers
    total_a = int(input())
    total_b = int(input())
    group_size = int(input())
    
    # Calculate effective group values
    value_a = calculate_groups(total_a, group_size)
    value_b = calculate_groups(total_b, group_size)
    
    # Calculate the result as a product of the two values
    result = value_a * value_b
    
    # Output the resulting product
    print(result)


if __name__ == "__main__":
    main()
