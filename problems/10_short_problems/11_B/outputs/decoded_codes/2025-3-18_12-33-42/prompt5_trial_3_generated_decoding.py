# This program finds a non-negative integer i such that the sum of the first i natural numbers meets or exceeds a given number n

# Accept user input and process it
target_value = abs(int(input()))  # Take absolute value of user input

# Initialize counter for natural numbers
current_index = 0

# Start an infinite loop to calculate sums
while True:
    # Calculate the sum of the first current_index natural numbers
    current_sum = current_index * (current_index + 1) // 2
    
    # Calculate the difference between current_sum and target_value
    remainder = current_sum - target_value

    # Check if the current_sum is equal to target_value
    if current_sum == target_value:
        print(current_index)  # Found the desired index
        break  # Exit the loop
    # Check if the current_sum is greater than target_value
    elif current_sum > target_value:
        # Check if the remainder is even
        if remainder % 2 == 0:
            print(current_index)  # Found the desired index
            break  # Exit the loop

    # Increment the counter for the next iteration
    current_index += 1
