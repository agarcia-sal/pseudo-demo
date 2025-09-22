# This code determines the index of a triangular number that matches the user's input or can be derived from it.

def find_triangular_number_index():
    # Read an integer input from the user and take its absolute value
    user_input = abs(int(input()))
    index = 0

    # Infinite loop to find the triangular number condition
    while True:
        # Calculate the current triangular number
        triangular_number = (index * (index + 1)) // 2
        
        # Calculate the difference from the input
        difference = triangular_number - user_input

        # Check if we have found a match
        if triangular_number == user_input:
            print(index)  # Output the current index
            break  # Exit the loop

        # Check if the triangular number exceeds the input
        elif triangular_number > user_input:
            # Check if the difference is even
            if difference % 2 == 0:
                print(index)  # Output the current index
                break  # Exit the loop

        # Increment index for the next triangular number calculation
        index += 1

# Example execution
find_triangular_number_index()
