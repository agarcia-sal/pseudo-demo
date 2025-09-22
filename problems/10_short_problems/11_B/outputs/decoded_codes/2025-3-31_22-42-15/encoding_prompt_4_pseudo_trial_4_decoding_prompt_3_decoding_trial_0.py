def find_index():
    # Prompt the user for input and store the absolute value of the integer
    number = abs(int(input()))
    
    # Initialize a counter variable
    index = 0
    
    # Infinite loop to find the solution
    while True:
        # Calculate the sum of the first 'index' integers
        current_sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the input number
        difference = current_sum - number
        
        # Check if the sum equals the input number
        if current_sum == number:
            print(index)  # Output the index
            break  # Exit the loop
        
        # Check if the sum exceeds the input number
        elif current_sum > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Exit the loop
        
        # Increment the counter variable
        index += 1

# Call the function to execute the logic
find_index()
