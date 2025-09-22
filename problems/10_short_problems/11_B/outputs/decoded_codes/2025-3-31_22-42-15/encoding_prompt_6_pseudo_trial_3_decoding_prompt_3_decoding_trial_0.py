def find_matching_index():
    # Read an integer input from the user and take its absolute value.
    user_input = abs(int(input()))

    # Initialize a variable to keep track of the current index.
    index = 0

    # Continuously loop until a condition is met.
    while True:
        # Calculate the sum of the first 'index' integers using the formula for the sum of an arithmetic series.
        total_sum = (index * (index + 1)) // 2
        
        # Determine the difference between the calculated sum and the user input.
        difference = total_sum - user_input
        
        # Check if the calculated sum is equal to the user input.
        if total_sum == user_input:
            # If they are equal, print the current index and exit the loop.
            print(index)
            break
        
        # Check if the calculated sum exceeds the user input.
        elif total_sum > user_input:
            # If the difference is even, print the current index and exit the loop.
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index to check the next integer in the next iteration.
        index += 1

# Example usage
find_matching_index()
