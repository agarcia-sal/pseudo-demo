def main():
    # Read inputs: total items, another quantity, and maximum items per group
    total_items = int(input())
    another_quantity = int(input())
    max_items_per_group = int(input())

    # Calculate the final result by calling the helper function for both total_items and another_quantity
    result = (calculate_groups(total_items, max_items_per_group) *
              calculate_groups(another_quantity, max_items_per_group))

    # Output the calculated result
    print(result)

def calculate_groups(item_count, items_per_group):
    """
    Calculate the total items in the formed groups.
    
    Parameters:
    item_count (int): The total number of items.
    items_per_group (int): The maximum items that can be placed in a single group.

    Returns:
    int: Total items counted, depending on complete groups and remaining items.
    """
    # Determine how many full groups can be formed and the number of remaining items
    number_of_full_groups, remaining_items = divmod(item_count, items_per_group)

    # If there are remaining items, return total items in those groups
    if remaining_items > 0:
        return remaining_items * (number_of_full_groups + 1)
    else:
        # If no remaining items, return the original item count
        return item_count

# Entry point of the program
if __name__ == "__main__":
    main()
