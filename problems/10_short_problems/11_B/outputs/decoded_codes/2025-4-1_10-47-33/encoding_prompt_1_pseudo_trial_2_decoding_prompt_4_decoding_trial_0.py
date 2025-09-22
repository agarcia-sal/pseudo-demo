# Read a number from the user and store its absolute value
absolute_input = abs(int(input()))

# Initialize a counter
index = 0

# Infinite loop for calculation
while True:
    # Calculate the sum of the first 'index' integers
    current_sum = (index * (index + 1)) // 2
    
    # Calculate the difference between 'current_sum' and 'absolute_input'
    difference = current_sum - absolute_input
    
    # Check conditions
    if current_sum == absolute_input:
        # If current_sum is equal to absolute_input
        print(index)  # Output the value of index as the result
        break  # Exit the loop
    elif current_sum > absolute_input:
        # If current_sum is greater than absolute_input
        if difference % 2 == 0:
            # If difference is an even number
            print(index)  # Output the value of index as the result
            break  # Exit the loop
    
    # Increment the counter
    index += 1
