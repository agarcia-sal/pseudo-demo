def find_number_matching_condition():
    # Get the absolute value of user input and convert it to an integer
    userInput = abs(int(input()))
    
    # Initialize the counter variable
    index = 0
    
    # Loop indefinitely until a break condition is met
    while True:
        # Calculate the sum of the first 'index' natural numbers using the formula for triangular numbers
        sum = (index * (index + 1)) // 2
        
        # Calculate the difference between 'sum' and 'userInput'
        difference = sum - userInput
        
        # Check if the sum equals the user input
        if sum == userInput:
            print(index)  # Print the index if sum matches user input
            break  # Exit the loop
        
        # Check if the sum exceeds the user input
        elif sum > userInput:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index if the difference is even
                break  # Exit the loop
        
        # Increment the index for the next iteration
        index += 1

# Call the function to execute
find_number_matching_condition()
