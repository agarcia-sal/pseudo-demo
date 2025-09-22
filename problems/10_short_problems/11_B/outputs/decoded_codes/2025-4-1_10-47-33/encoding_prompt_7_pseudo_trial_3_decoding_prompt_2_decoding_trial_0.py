def findIntegerWithTriangleNumber(inputValue):
    # Step 1: Prepare the input value
    absoluteValue = abs(inputValue)
    
    # Step 2: Initialize a counter variable
    counter = 0
    
    # Step 3: Begin an infinite loop to calculate triangular numbers
    while True:
        # Calculate the current triangular number using the formula
        triangularNumber = (counter * (counter + 1)) // 2
        
        # Calculate the difference between the triangular number and the absolute value
        difference = triangularNumber - absoluteValue
        
        # Step 4: Check if the triangular number equals the absolute value
        if triangularNumber == absoluteValue:
            print(counter)  # Found a match, output the counter
            break  # Exit the loop
            
        # Step 5: Check if the triangular number is greater than the absolute value
        elif triangularNumber > absoluteValue:
            # Check if the difference is even
            if difference % 2 == 0:
                print(counter)  # Found a match, output the counter
                break  # Exit the loop
        
        # Increment the counter for the next triangular number
        counter += 1
