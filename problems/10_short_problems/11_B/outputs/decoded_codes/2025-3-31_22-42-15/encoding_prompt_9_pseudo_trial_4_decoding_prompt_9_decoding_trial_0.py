# Begin the program
absolute_value = abs(int(input()))  # Get the absolute value of the user input
current_index = 0  # Initialize the current index

# Start looping indefinitely
while True:
    # Calculate the sum of the first current_index natural numbers
    sum_of_numbers = (current_index * (current_index + 1)) // 2
    # Calculate the difference between the sum and absolute value
    difference = sum_of_numbers - absolute_value
    
    # Check if the sum equals the absolute value
    if sum_of_numbers == absolute_value:
        print(current_index)  # Output current index
        break  # Exit the loop
    # Check if the sum exceeds the absolute value
    elif sum_of_numbers > absolute_value:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_index)  # Output current index
            break  # Exit the loop
    
    current_index += 1  # Increment current index for the next iteration
