# Start the program
def find_integer():
    # Get user input
    target_value = int(input())  # Read an integer value from the user
    target_value = abs(target_value)  # Calculate the absolute value of target_value

    # Initialize variables
    current_index = 0  # Set a counter variable to 0

    # Begin infinite loop
    while True:
        # Calculate the sum of the first 'current_index' integers
        sum_of_integers = (current_index * (current_index + 1)) // 2
        
        # Calculate the difference
        difference = sum_of_integers - target_value
        
        # Check conditions
        if sum_of_integers == target_value:
            print(current_index)  # Print current_index when the sum matches target_value
            break
        elif sum_of_integers > target_value:
            if difference % 2 == 0:  # Check if the difference is evenly divisible by 2
                print(current_index)  # Print current_index when conditions are met
                break
        
        # Increment current_index by 1 to check the next integer
        current_index += 1

# Call the function to execute the program
find_integer()
