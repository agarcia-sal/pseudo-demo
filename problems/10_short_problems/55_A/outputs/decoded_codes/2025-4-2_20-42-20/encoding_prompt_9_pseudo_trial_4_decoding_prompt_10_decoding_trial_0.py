def process_boolean_list():
    # Receive input for the size of the boolean list
    n = int(input())
    
    # Initialize the boolean list with all True values
    boolean_list = [True] * n
    index = 0  # This will track the current position in the list
    counter = 1  # This will determine how far to move in each iteration

    # Loop through a range until counter exceeds 500,000
    while counter <= 500000:
        if boolean_list[index]:  # Check if the current index is True
            boolean_list[index] = False  # Mark this position as processed
        
        counter += 1  # Increment the counter
        index = (index + counter) % n  # Update index with wrap-around using modulo

    # Gather all remaining True values
    remaining_true_values = [value for value in boolean_list if value]

    # Check the length of remaining true values
    if len(remaining_true_values) == 0:
        print("YES")  # Print "YES" if all values have been processed
    else:
        print("NO")  # Print "NO" if some values remain True

# Call the main function to execute the logic
process_boolean_list()
