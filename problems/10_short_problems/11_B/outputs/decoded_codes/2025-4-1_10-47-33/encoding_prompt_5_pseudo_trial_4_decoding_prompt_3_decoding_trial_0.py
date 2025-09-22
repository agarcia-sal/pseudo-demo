def find_smallest_integer():
    # Get the absolute value of input number
    number = abs(int(input()))
    
    # Initialize a counter variable
    index = 0
    
    # Continuously search for a valid integer
    while True:
        # Calculate the current triangular number
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the input number
        difference = triangular_number - number
        
        # Check if the triangular number equals the input number
        if triangular_number == number:
            print(index)
            break
        
        # Check if the triangular number is greater than the input number
        elif triangular_number > number:
            # Verify if the difference is even
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next triangular number
        index += 1

# You can call the function to test its functionality
# find_smallest_integer()  # Uncomment this line to test
