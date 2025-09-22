# Start the program

# Get user input and convert it to an absolute value
target_number = abs(int(input()))

# Initialize the counter for the index
current_index = 0

# Loop until the condition is satisfied
while True:
    # Calculate the sum of integers from 0 to current_index
    current_sum = sum(range(current_index + 1))  # Sum of 0 to current_index
    
    # Calculate the difference from the target number
    difference = current_sum - target_number

    # Check if the current sum equals the target number
    if current_sum == target_number:
        print(current_index)  # Print current index as it is the answer
        break  # End the program
    
    # Check if the current sum exceeds the target number
    if current_sum > target_number:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_index)  # Print current index as it is also an answer
            break  # End the program
    
    # Increment the current index by 1 for the next iteration
    current_index += 1

# End the program
