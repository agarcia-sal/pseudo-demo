def find_least_integer():
    # Read the input and convert it to an absolute integer
    absolute_value = abs(int(input()))
    index = 0  # This will be used to calculate triangular numbers

    # Start an infinite loop to find the required integer
    while True:
        # Calculate the triangular number using the formula
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the absolute value
        difference = triangular_number - absolute_value
        
        # Check if the triangular number matches the absolute value
        if triangular_number == absolute_value:
            print(index)
            break
        
        # Check if the triangular number exceeds the absolute value
        if triangular_number > absolute_value:
            # If the difference is even, output the index
            if difference % 2 == 0:
                print(index)
                break
        
        # Increment the index for the next iteration
        index += 1

# You can now call the function to execute
# Uncomment the following line to run the function
# find_least_integer()
