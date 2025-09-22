def FindIntegerSolution():
    # Step 1: Read an integer input and take the absolute value of it
    targetValue = abs(int(input()))
    
    # Step 2: Initialize a counter variable
    index = 0
    
    # Step 3: Enter an infinite loop to find the solution
    while True:
        # Calculate the sum of the first 'index' integers
        sum_value = (index * (index + 1)) // 2
        
        # Calculate the difference between the sum and the target value
        difference = sum_value - targetValue
        
        # Step 4: Check if the sum equals the target value
        if sum_value == targetValue:
            print(index)
            break
            
        # Check if the sum exceeds the target value
        elif sum_value > targetValue:
            # If the difference is even, we found a valid solution
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1
