# Start of the program

# Get User Input
# Read an integer input from the user and convert it to its absolute value
target_number = abs(int(input()))

# Initialize Counter
current_index = 0

# Loop Until a Condition is Met
while True:
    # Calculate the sum of all integers from 0 to current_index
    current_sum = (current_index * (current_index + 1)) // 2
    
    # Calculate the difference between current_sum and target_number
    difference = current_sum - target_number

    # Check Conditions
    if current_sum == target_number:
        # If current_sum equals target_number, print current_index
        print(current_index)
        break

    elif current_sum > target_number:
        # If current_sum is greater than target_number, check if the difference is even
        if difference % 2 == 0:
            # If the difference is even, print current_index
            print(current_index)
            break
    
    # Increment current_index by 1 for the next iteration
    current_index += 1

# End of the program
