# Start the program
# Input: Read an integer value from the user and store its absolute value
target_sum = abs(int(input()))

# Initialize a counter
index = 0

# Loop: Begin an infinite loop that continues until a break condition is met
while True:
    # Calculate currentSum using the formula for the sum of the first index natural numbers
    current_sum = index * (index + 1) // 2  # Using integer division for clarity

    # Calculate the difference between currentSum and targetSum
    difference = current_sum - target_sum
    
    # Check for exact match
    if current_sum == target_sum:
        print(index)  # Output the value of index
        break  # Terminate the loop
    
    # Check for overshoot
    if current_sum > target_sum:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the value of index
            break  # Terminate the loop

    # Increment the index
    index += 1

# End of the program
