def calculate_groups(item_count, items_per_group):
    # Determine how many complete groups can be formed and any remaining items
    number_of_full_groups = item_count // items_per_group
    remaining_items = item_count % items_per_group

    # If there are remaining items, return the total items in those groups
    if remaining_items > 0:
        return remaining_items * (number_of_full_groups + 1)
    else:
        # If there are no remaining items, return the original item_count
        return item_count

def main():
    # Read inputs: total items, another quantity, and maximum items per group
    total_items = int(input())
    another_quantity = int(input())
    max_items_per_group = int(input())

    # Calculate the final result by calling the helper function for both total_items and another_quantity
    result = calculate_groups(total_items, max_items_per_group) * calculate_groups(another_quantity, max_items_per_group)

    # Output the calculated result
    print(result)

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
