def find_triangular_index():
    # Read an integer input and get its absolute value
    number = abs(int(input()))

    # Initialize counter
    index = 0

    # Infinite loop to find the desired value
    while True:
        # Calculate the triangular number for the current index
        triangular_number = (index * (index + 1)) // 2

        # Calculate the difference between the triangular number and the input number
        difference = triangular_number - number

        # Check if the triangular number equals the input number
        if triangular_number == number:
            print(index)
            break

        # Check if the triangular number exceeds the input number
        elif triangular_number > number:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)
                break

        # Increment the index for the next iteration
        index += 1

# Call the function to execute
find_triangular_index()
