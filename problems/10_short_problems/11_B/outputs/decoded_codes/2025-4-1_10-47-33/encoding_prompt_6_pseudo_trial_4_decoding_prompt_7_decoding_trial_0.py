# Begin the program

# Read an integer input and take its absolute value
absolute_value = abs(int(input()))

# Initialize a counter variable
counter = 0

# Loop indefinitely until a break condition is met
while True:
    # Calculate the sum of the first 'counter' integers
    current_sum = (counter * (counter + 1)) // 2
    
    # Calculate the difference between current_sum and absolute_value
    difference = current_sum - absolute_value
    
    # Check if the current_sum equals the absolute_value
    if current_sum == absolute_value:
        # Output the counter value
        print(counter)
        break  # Exit the loop

    # Check if current_sum exceeds absolute_value
    elif current_sum > absolute_value:
        # Check if the difference is even
        if difference % 2 == 0:
            # Output the counter value
            print(counter)
            break  # Exit the loop

    # Increment the counter for the next iteration
    counter += 1
