def calculate_groups(total_quantity, group_size):
    """
    Calculate the effective number of groups that can be formed from
    a given total quantity and group size.

    Parameters:
    total_quantity (int): The total quantity of items.
    group_size (int): The size of each group.

    Returns:
    int: The effective number of groups.
    """
    full_groups = total_quantity // group_size  # Integer division to find full groups
    remainder = total_quantity % group_size      # Remainder to find extra items

    if remainder > 0:
        return remainder * (full_groups + 1)     # Effective groups if there are extra items
    else:
        return total_quantity                      # Return total quantity if no extra items

def main():
    # Read input values for the quantities and group size
    quantity1 = int(input())
    quantity2 = int(input())
    group_size = int(input())
    
    # Calculate effective group values for both quantities
    effective_groups1 = calculate_groups(quantity1, group_size)
    effective_groups2 = calculate_groups(quantity2, group_size)

    # Multiply the two effective group values together
    final_result = effective_groups1 * effective_groups2
    
    # Output the final result
    print(final_result)

# Entry point of the program
if __name__ == "__main__":
    main()
