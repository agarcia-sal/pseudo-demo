def FindIntegerBasedOnInput():
    # Prompt user for input and convert it to an absolute integer
    inputNumber = abs(int(input()))
    
    # Initialize index to start from 0
    index = 0
    
    # Begin an infinite loop to calculate sums
    while True:
        # Calculate the sum of the first 'index' integers using the formula
        sum_value = (index * (index + 1)) // 2  # Using integer division
        
        # Calculate the difference between sum and inputNumber
        difference = sum_value - inputNumber
        
        # Check if the sum equals the inputNumber
        if sum_value == inputNumber:
            print(index)  # Output the current index
            break  # Exit the loop
        
        # Check if the sum is greater than the inputNumber
        elif sum_value > inputNumber:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop
        
        # Increment index to evaluate the next integer
        index += 1

# Invocation of the function
FindIntegerBasedOnInput()
