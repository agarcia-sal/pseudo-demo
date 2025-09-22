# Begin the algorithm

# Take absolute integer input from the user
user_input = abs(int(input()))  # Get the absolute value of the input
index = 0  # Initialize index to 0

# Start an infinite loop
while True:
    # Calculate the sum of the first 'index' integers
    sum_of_first_index = (index * (index + 1)) // 2  # Use integer division
    
    # Calculate the difference between the sum and the user input
    difference = sum_of_first_index - user_input
    
    # Check if the sum is equal to the user input
    if sum_of_first_index == user_input:
        # Print the current index and exit the loop
        print(index)
        break  # Exit the loop
    
    # Check if the sum is greater than the user input
    elif sum_of_first_index > user_input:
        # Check if the difference is even
        if difference % 2 == 0:  # Use modulus operator to check for even
            # Print the current index and exit the loop
            print(index)
            break  # Exit the loop
    
    # Increment index by 1 for the next iteration
    index += 1  # Increment index by 1

# End of algorithm
