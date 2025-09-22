# Start the program

# Input the Number
target_sum = abs(int(input()))  # Read input and convert it to an absolute integer

# Initialize Counter
index = 0  # Set counter to zero

# Begin Infinite Loop
while True:
    # Calculate the Sum of the First 'index' Integers
    current_sum = (index * (index + 1)) // 2  # Calculate the current sum using the formula

    # Calculate the Difference
    difference = current_sum - target_sum  # Calculate the difference

    # Check for Equality
    if current_sum == target_sum:
        print(index)  # Output the index if the current sum matches the target sum
        break  # Exit the loop

    # Check for Exceeding the Target
    if current_sum > target_sum:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Output the index if the criteria are met
            break  # Exit the loop
    
    # Increment the Counter
    index += 1  # Increase index by 1 for the next iteration
