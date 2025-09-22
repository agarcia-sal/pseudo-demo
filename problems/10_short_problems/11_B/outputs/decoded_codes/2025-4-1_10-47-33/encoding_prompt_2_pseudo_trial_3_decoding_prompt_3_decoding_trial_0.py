# Function to find the index that satisfies the conditions based on the sum of integers
def find_index_based_on_sum():
    # Step 2: Receive an integer input from the user and take its absolute value
    target_number = abs(int(input()))
    
    # Step 3: Initialize the counter variable
    current_index = 0
    
    # Step 4: Enter an infinite loop to perform calculations
    while True:
        # Step 4a: Calculate the sum of integers from 0 to currentIndex
        sum_value = (current_index * (current_index + 1)) // 2
        
        # Step 4b: Determine the difference from the target
        difference_from_target = sum_value - target_number
        
        # Step 4c: Check if the sum equals the target number
        if sum_value == target_number:
            print(current_index)
            break  # Exit the loop if condition is met
        
        # Step 4d: If sum_value is greater than target_number
        if sum_value > target_number:
            # Check if the difference is even
            if difference_from_target % 2 == 0:
                print(current_index)
                break  # Exit the loop if condition is met
        
        # Step 4e: Increment the index for the next iteration
        current_index += 1

# Call the function to execute the program
find_index_based_on_sum()
