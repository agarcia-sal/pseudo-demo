def main():
    # Step 1: Get the number of items from input
    number_of_items = int(input())
    
    # Step 2: Initialize a list to track active items
    is_active = [True] * number_of_items
    
    # Step 3: Initialize current position and step count
    current_position = 0
    step_count = 1
    
    # Step 4: Loop until step_count exceeds 500,000
    while step_count <= 500000:
        if is_active[current_position]:  # Check if the item is active
            is_active[current_position] = False  # Mark the item as inactive
            
            # Increment step_count and update current_position
            step_count += 1
            current_position = (current_position + step_count) % number_of_items  # Wrap around using modulus
    
    # Step 5: Create a list of remaining active items
    remaining_active_items = [active for active in is_active if active]
    
    # Step 6: Check if there are any remaining active items
    if len(remaining_active_items) == 0:
        print("YES")
    else:
        print("NO")

# Ensure that the main function only runs when the script is executed
if __name__ == "__main__":
    main()
