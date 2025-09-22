# Start of the program

# Step 2: Read an integer value from the user and take its absolute value
target_number = abs(int(input()))  # Read input and convert it to an absolute integer

# Step 3: Initialize currentIndex to 0
current_index = 0

# Step 4: Enter an infinite loop
while True:
    # Calculate the sum of the first currentIndex natural numbers
    current_sum = sum(range(current_index + 1))  # Using sum of range to calculate the current sum
    
    # Calculate the difference between currentSum and targetNumber
    difference = current_sum - target_number
    
    # If currentSum is equal to targetNumber
    if current_sum == target_number:
        print(current_index)  # Display currentIndex as the result
        break  # Exit the loop
        
    # Else if currentSum is greater than targetNumber
    elif current_sum > target_number:
        # Check if the difference is an even number
        if difference % 2 == 0:  # If difference is even
            print(current_index)  # Display currentIndex as the result
            break  # Exit the loop
    
    # Increment currentIndex by 1
    current_index += 1  # Move to the next natural number

# End of the program
