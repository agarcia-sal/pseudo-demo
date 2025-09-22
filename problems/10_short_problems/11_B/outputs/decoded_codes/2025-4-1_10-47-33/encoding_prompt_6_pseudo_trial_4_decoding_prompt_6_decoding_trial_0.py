# Begin by reading an integer input and converting it to its absolute value
absolute_value = abs(int(input()))

# Initialize a counter variable
counter = 0

# Loop indefinitely until the break condition is met
while True:
    # Calculate the sum of the first 'counter' integers using the formula
    current_sum = (counter * (counter + 1)) // 2
    
    # Calculate the difference between current_sum and absolute_value
    difference = current_sum - absolute_value
    
    # Check if current_sum equals absolute_value
    if current_sum == absolute_value:
        print(counter)  # Output the counter value
        break  # Exit the loop
    
    # Check if current_sum exceeds absolute_value
    elif current_sum > absolute_value:
        # Check if the difference is even
        if difference % 2 == 0:
            print(counter)  # Output the counter value
            break  # Exit the loop
    
    # Increment the counter for the next iteration
    counter += 1
