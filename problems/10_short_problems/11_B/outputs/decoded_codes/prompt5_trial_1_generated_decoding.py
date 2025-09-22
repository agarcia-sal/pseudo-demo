def find_smallest_triangular_index():
    # Accept an integer input from the user and ensure it's non-negative
    user_input = input()
    number = abs(int(user_input))

    # Initialize a counter variable for the triangular number index
    index = 0

    # Continuously calculate triangular numbers until a condition is met
    while True:
        # Calculate the current triangular number using the formula n(n + 1) / 2
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference between the triangular number and the input number
        difference = triangular_number - number

        # Check if the triangular number is equal to the input number
        if triangular_number == number:
            # If they are equal, output the current index
            print(index)
            break
        
        # Check if the triangular number exceeds the input number
        elif triangular_number > number:
            # Check if the difference is even
            if difference % 2 == 0:
                # If the difference is even, output the current index
                print(index)
                break
        
        # Increment the index for the next triangular number calculation
        index += 1

# Example of calling the function (uncomment to test)
# find_smallest_triangular_index()
