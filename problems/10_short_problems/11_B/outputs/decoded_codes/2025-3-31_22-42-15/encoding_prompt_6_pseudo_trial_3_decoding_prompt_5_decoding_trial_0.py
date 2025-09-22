# Function to find the index based on user input
def find_index():
    # Read an integer input from the user and take its absolute value
    user_input = abs(int(input()))

    # Initialize a variable to keep track of the current index
    index = 0

    # Continuously loop until a condition is met
    while True:
        # Calculate the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2
        
        # Determine the difference between the calculated sum and user input
        difference = current_sum - user_input
        
        # Check if the calculated sum is equal to the user input
        if current_sum == user_input:
            # Print the current index and exit the loop
            print(index)
            break
        
        # Check if the calculated sum exceeds the user input
        elif current_sum > user_input:
            # If the difference is even
            if difference % 2 == 0:
                # Print the current index and exit the loop
                print(index)
                break
        
        # Increment the index to check the next integer in the next iteration
        index += 1

# Call the function to execute
find_index()
