def calculate_items_needed(total_items, group_size):
    """
    Calculate the total items needed based on how many complete groups can be formed.
    
    Parameters:
    total_items (int): The total number of items available.
    group_size (int): The size of the group.
    
    Returns:
    int: Total items needed based on the group formation.
    """
    complete_groups = total_items // group_size
    remainder = total_items % group_size

    if remainder > 0:
        # If there is a remainder, calculate additional items needed
        items_needed = (complete_groups + 1) * remainder
    else:
        # If no remainder, return the total items as is
        items_needed = total_items

    return items_needed


def main():
    # Read input values for two cases
    total_items_for_first_case = int(input())
    total_items_for_second_case = int(input())
    group_size = int(input())

    # Calculate results for both cases
    first_result = calculate_items_needed(total_items_for_first_case, group_size)
    second_result = calculate_items_needed(total_items_for_second_case, group_size)

    # Output the final product of both results
    final_result = first_result * second_result
    print(final_result)


# Start the program
if __name__ == "__main__":
    main()
