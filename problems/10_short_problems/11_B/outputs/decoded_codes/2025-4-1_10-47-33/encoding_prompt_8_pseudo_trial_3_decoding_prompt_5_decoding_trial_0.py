def find_smallest_integer():
    # Read input and take absolute value
    target_number = abs(int(input()))
    index = 0  # Initialize the index variable

    while True:  # Start an infinite loop
        # Calculate the sum of integers from 0 to index
        sum_to_index = (index * (index + 1)) // 2
        
        # Calculate the difference between sum_to_index and target_number
        difference = sum_to_index - target_number
        
        # Check if the sum matches the target number
        if sum_to_index == target_number:
            print(index)  # Print the index if there's an exact match
            break  # Exit the loop

        # Check if the sum exceeds the target number
        if sum_to_index > target_number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index if the difference is even
                break  # Exit the loop
        
        index += 1  # Increment the index by 1 for the next iteration

# Call the function to execute
find_smallest_integer()
