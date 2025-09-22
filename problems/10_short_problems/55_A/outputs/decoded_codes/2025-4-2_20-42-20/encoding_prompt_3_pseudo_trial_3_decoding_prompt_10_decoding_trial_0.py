def main():
    # Read an integer input representing the size of the list
    size_to_check = int(input())
    
    # Initialize a list to track boolean values for numbers up to size_to_check
    is_checked = [True] * size_to_check

    # Initialize counter variable
    index = 0
    increment = 1

    # Loop while increment is less than or equal to 500,000
    while increment <= 500000:
        # If the current position (index) in the list is still True
        if is_checked[index]:
            # Mark the current position as False (checked)
            is_checked[index] = False
        
        # Increment the value of increment
        increment += 1
        
        # Update the index based on the current increment value
        index = (index + increment) % size_to_check

    # Create a filtered list of items in is_checked that are still True
    remaining_true_items = [item for item in is_checked if item]

    # Check if there are any True values left in the remaining_true_items list
    if len(remaining_true_items) == 0:
        # If no True items are left, print 'YES'
        print('YES')
    else:
        # If there are True items left, print 'NO'
        print('NO')

# Run the main function
if __name__ == "__main__":
    main()
