def findSuitableInteger():
    # Read and convert the user input to an absolute integer
    userInput = abs(int(input()))
    index = 0

    # Start an infinite loop to find the suitable integer
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum_value = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the user input
        difference = sum_value - userInput
        
        # Check if the calculated sum equals the user input
        if sum_value == userInput:
            print(index)  # Print the index if found
            break  # Exit the loop
        # Check if the calculated sum is greater than the user input
        elif sum_value > userInput:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index if found
                break  # Exit the loop
        
        # Increment the index for the next iteration
        index += 1
