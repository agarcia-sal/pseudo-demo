def find_index_for_sum():
    # Step 1: Read an integer input from the user
    user_input = abs(int(input()))
    index = 0

    # Step 2: Infinite loop to find the required index
    while True:
        # Calculate the sum of the first 'index' natural numbers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference from the user input
        difference = current_sum - user_input
        
        # Step 3: Check if we found the desired sum
        if current_sum == user_input:
            print(index)
            break
        
        # Step 4: If sum is greater than user input
        elif current_sum > user_input:
            # Step 5: Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Step 6: Increment index for the next iteration
        index += 1

# Call the function to execute the logic
find_index_for_sum()
