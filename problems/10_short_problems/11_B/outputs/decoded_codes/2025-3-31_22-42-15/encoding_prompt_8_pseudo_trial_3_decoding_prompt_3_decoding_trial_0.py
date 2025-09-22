def find_integer():
    # Get user input
    target_value = int(input())
    target_value = abs(target_value)  # Ensure we are working with a non-negative integer

    current_index = 0  # Initialize counter variable

    # Begin infinite loop
    while True:
        # Calculate the sum of the first 'current_index' integers
        sum_of_integers = (current_index * (current_index + 1)) // 2  # Use integer division

        # Calculate the difference between the sum and target value
        difference = sum_of_integers - target_value
        
        # Check conditions
        if sum_of_integers == target_value:
            print(current_index)  # Print the current index if it matches
            break  # Exit the loop

        if sum_of_integers > target_value:
            if difference % 2 == 0:  # Check if the difference can be evenly divided by 2
                print(current_index)  # Print the current index if the condition is met
                break  # Exit the loop

        current_index += 1  # Increment the count for the next loop iteration

# Call the function to execute
find_integer()
