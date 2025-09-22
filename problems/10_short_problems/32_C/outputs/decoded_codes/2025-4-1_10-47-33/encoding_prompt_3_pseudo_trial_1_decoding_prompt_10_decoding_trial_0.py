def mc(total_items, group_size):
    """
    Calculates the effective number of items based on total items and group size.
    
    Parameters:
    total_items (int): The total number of items.
    group_size (int): The size of each group.
    
    Returns:
    int: The effective count of items to consider.
    """
    # Calculate how many full groups can fit
    full_groups, remainder = divmod(total_items, group_size)

    # Determine the effective item count based on remainder
    if remainder > 0:
        return remainder * (full_groups + 1)  # Count remainder items with an additional group
    else:
        return total_items  # No remainder, return total item count

def main():
    # Read input values for total items n, additional total m, and group size s
    total_items_n = int(input())
    additional_total_m = int(input())
    group_size_s = int(input())
    
    # Calculate and print the product of the processed item counts for n and m
    result = mc(total_items_n, group_size_s) * mc(additional_total_m, group_size_s)
    print(result)

if __name__ == "__main__":
    main()


     10
     20
     5
     

     7
     3
     2
     

     15
     15
     5
     