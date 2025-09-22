def findTriangleNumberIndex():
    # Get the absolute value of the user input as an integer
    inputValue = abs(int(input()))
    
    # Initialize the index variable
    index = 0
    
    # Infinite loop to find the triangle number index
    while True:
        # Calculate the ith triangle number using the formula
        triangleNumber = (index * (index + 1)) / 2
        
        # Calculate the difference between the triangle number and the input value
        difference = triangleNumber - inputValue
        
        # Check if the triangle number equals the input value
        if triangleNumber == inputValue:
            # Print the index if a match is found
            print(index)
            break  # Exit the loop
            
        # If the triangle number exceeds the input value
        elif triangleNumber > inputValue:
            # Check if the difference is even
            if difference % 2 == 0:
                # Print the index if the difference is even
                print(index)
                break  # Exit the loop
        
        # Increment the index for the next iteration
        index += 1
