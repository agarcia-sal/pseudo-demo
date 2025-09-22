def main():
    # Step 1: Get the total number of elements from user input
    total_elements = int(input())
    
    # Step 2: Create a list initialized to True to track statuses
    boolean_list = [True] * total_elements
    
    # Step 3: Initialize current index and increment
    current_index = 0
    increment = 1

    # Step 4: Loop until increment exceeds 500,000
    while increment <= 500000:
        # Step 5: Check if the current position in boolean list is true
        if boolean_list[current_index]:
            # Set the position in boolean list to false
            boolean_list[current_index] = False
        
        # Increment the increment value
        increment += 1
        
        # Update the current index with correct wrapping
        current_index = (current_index + increment) % total_elements
    
    # Step 6: Extract all values that remain true
    remaining_true_values = [value for value in boolean_list if value]
    
    # Step 7: Check the number of remaining true values
    if len(remaining_true_values) == 0:
        print("YES")
    else:
        print("NO")

# Step 8: Run the main function
if __name__ == "__main__":
    main()
