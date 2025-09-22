def find_integer_based_on_triangular_number():
    # Read an integer input and ensure it is positive
    positive_integer = abs(int(input()))

    # Initialize a counter variable
    index = 0

    # Start an infinite loop to calculate triangular numbers
    while True:
        # Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the input
        difference = triangular_number - positive_integer
        
        # Check if the triangular number is equal to the input
        if triangular_number == positive_integer:
            print(index)    # Output the index if it matches
            break          # Exit the loop
        
        # Check if the triangular number is greater than the input
        elif triangular_number > positive_integer:
            # Check if the difference is an even number
            if difference % 2 == 0:
                print(index)    # Output the index if the difference is even
                break          # Exit the loop
        
        # Increment the index for the next iteration
        index += 1

# To run the function, uncomment the line below
# find_integer_based_on_triangular_number()
