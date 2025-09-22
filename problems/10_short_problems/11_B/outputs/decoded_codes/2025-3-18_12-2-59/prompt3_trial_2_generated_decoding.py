def find_triangular_index():
    # Read input and convert to a positive integer
    input_value = abs(int(input()))
    
    # Initialize a counter for the triangular number index
    index = 0

    # Start an infinite loop to find the correct triangular number
    while True:
        # Calculate the current triangular number using the formula n(n+1)/2
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the input value
        difference = triangular_number - input_value

        # Check if the triangular number equals the input value
        if triangular_number == input_value:
            # If they are equal, print the index and exit the loop
            print(index)
            break

        # Check if the triangular number exceeds the input value
        elif triangular_number > input_value:
            # Check if the difference is even
            if difference % 2 == 0:
                # If the difference is even, print the index and exit the loop
                print(index)
                break
        
        # Increment the index for the next triangular number calculation
        index += 1

# Call the function to execute the code
find_triangular_index()
