def findIntegerForTriangularNumber():
    # Prompt user for input and store as absolute integer 'number'
    number = abs(int(input()))
    
    # Initialize 'index' to 0
    index = 0

    # Start an infinite loop
    while True:
        # Calculate the triangular number using the formula
        triangularSum = (index * (index + 1)) // 2
        
        # Calculate the difference between triangularSum and number
        difference = triangularSum - number
        
        # Check if the triangular number equals the input number
        if triangularSum == number:
            print(index)  # Output the index
            break  # Exit the loop

        # Check if the triangular number is greater than the input number
        elif triangularSum > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the index
                break  # Exit the loop
        
        # Increment index for the next iteration
        index += 1

# Example of running the function (uncomment below to run)
# findIntegerForTriangularNumber()
