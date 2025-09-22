def FindSmallestInteger():
    # Get absolute value of an input number
    number = abs(int(input()))
    
    # Initialize a counter variable
    index = 0
    
    # Continuously search for a valid integer
    while True:
        # Calculate the current triangular number
        triangularNumber = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the input number
        difference = triangularNumber - number
        
        # Check if the triangular number equals the input number
        if triangularNumber == number:
            print(index)
            break
        
        # Check if the triangular number is greater than the input number
        elif triangularNumber > number:
            # Verify if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next triangular number
        index += 1
