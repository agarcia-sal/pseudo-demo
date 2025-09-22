def FindIntegerBasedOnSum():
    # Read the input value and convert it to an absolute integer
    inputValue = int(input())
    absoluteInput = abs(inputValue)

    # Initialize an index variable
    index = 0

    # Continuously loop to find a solution
    while True:
        # Calculate the sum of the first 'index' integers using the formula for the sum of the first n integers
        sum = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the absolute input
        difference = sum - absoluteInput

        # Check if the sum is equal to the absolute input
        if sum == absoluteInput:
            print(index)
            break  # Exit the loop since we have found our answer
        
        # Check if the sum is greater than the absolute input
        elif sum > absoluteInput:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break  # Exit the loop since we have found our answer
        
        # Increment the index for the next iteration
        index += 1

# Example test execution
FindIntegerBasedOnSum()
