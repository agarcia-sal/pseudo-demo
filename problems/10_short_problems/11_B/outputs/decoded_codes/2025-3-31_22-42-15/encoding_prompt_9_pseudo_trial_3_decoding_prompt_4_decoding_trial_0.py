def find_smallest_integer():
    # Step 1: Get Input
    target_sum = abs(int(input()))  # Read input as an integer and take its absolute value.

    # Step 2: Initialize a Counter
    current_index = 0

    # Step 3: Loop for Calculation
    while True:
        # Calculate the sum of the first current_index integers
        current_sum = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference
        difference = current_sum - target_sum
        
        # Check Conditions
        if current_sum == target_sum:
            print(current_index)  # Print current_index as it meets the condition
            break
        elif current_sum > target_sum:
            if difference % 2 == 0:  # Check if the difference is even
                print(current_index)  # Print current_index as it meets the condition
                break

        # Increment the currentIndex by 1
        current_index += 1

# Call the function to execute
find_smallest_integer()
