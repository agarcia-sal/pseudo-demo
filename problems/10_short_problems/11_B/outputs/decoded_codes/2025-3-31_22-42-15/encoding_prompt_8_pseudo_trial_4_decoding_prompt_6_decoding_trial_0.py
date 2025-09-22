# Get input from the user and store the absolute value in target_number
target_number = abs(int(input()))

# Initialize the counter to track the current integer
counter = 0

# Start an infinite loop
while True:
    # Calculate the sum of the first 'counter' integers
    current_sum = (counter * (counter + 1)) // 2
    
    # Calculate the difference between current_sum and target_number
    difference = current_sum - target_number
    
    # Check if the current_sum equals the target_number
    if current_sum == target_number:
        print(counter)  # Print counter if sums match
        break  # Exit the loop

    # Check if current_sum is greater than target_number
    if current_sum > target_number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(counter)  # Print counter if conditions are satisfied
            break  # Exit the loop

    # Increment counter for the next iteration
    counter += 1
