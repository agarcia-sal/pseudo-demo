def main():
    # Step 1: Initialize Input
    n = int(input())  # Get total number of boolean elements from the user

    # Step 2: Create Boolean List
    boolean_list = [True] * n  # Create a list of n elements, all initially set to True

    # Step 3: Set Initial Positions
    current_index = 0  # Current position in the boolean list
    increment = 1  # Increment that will help in updating the position
    limit = 500000  # Limit for the updates

    # Step 4: Update Loop
    while increment <= limit:
        if boolean_list[current_index]:  # If the value at current_index is True
            boolean_list[current_index] = False  # Change it to False
        
        increment += 1  # Increase the increment by 1
        current_index = (current_index + increment) % n  # Update current_index with wrap around using modulus

    # Step 5: Check Remaining True Values
    remaining_true = [value for value in boolean_list if value]  # Filter list for remaining True values

    # Step 6: Output Result
    if len(remaining_true) == 0:
        print('YES')  # If no True values are left
    else:
        print('NO')  # If some True values remain

# Run the main function
if __name__ == "__main__":
    main()
