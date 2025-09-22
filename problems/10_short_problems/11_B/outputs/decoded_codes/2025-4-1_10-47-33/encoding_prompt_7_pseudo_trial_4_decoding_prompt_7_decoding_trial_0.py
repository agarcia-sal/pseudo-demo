def findSuitableInteger():
    # Read and convert the user input to an absolute integer
    userInput = abs(int(input()))
    index = 0  # Initialize index

    # Start an infinite loop to find the suitable integer
    while True:
        # Calculate the sum of the first 'index' natural numbers
        sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the user input
        difference = sum - userInput
        
        # Check if the calculated sum equals the user input
        if sum == userInput:
            print(index)  # Print the index if found
            break  # Exit the loop
        
        # Check if the calculated sum is greater than the user input
        elif sum > userInput:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Print the index if found
                break  # Exit the loop
        
        # Increment the index for the next iteration
        index += 1

# Invoke the function to execute
findSuitableInteger()
