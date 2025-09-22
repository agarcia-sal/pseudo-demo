def find_index_for_sum():
    # Step 1: Read an integer input from the user
    user_input = abs(int(input()))  # Taking absolute value of the user input
    index = 0  # Initialize index

    # Step 2: Infinite loop to find the required index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_natural_numbers = (index * (index + 1)) // 2
        
        # Calculate the difference from the user input
        difference = sum_natural_numbers - user_input
        
        # Step 3: Check if we found the desired sum
        if sum_natural_numbers == user_input:
            print(index)
            break  # Exit the loop if the sum matches the user input
        
        # Step 4: If sum is greater than user input
        elif sum_natural_numbers > user_input:
            
            # Step 5: Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop if the difference is even
        
        # Step 6: Increment index for the next iteration
        index += 1  # Move to the next index

# Call the function to execute the logic
find_index_for_sum()
