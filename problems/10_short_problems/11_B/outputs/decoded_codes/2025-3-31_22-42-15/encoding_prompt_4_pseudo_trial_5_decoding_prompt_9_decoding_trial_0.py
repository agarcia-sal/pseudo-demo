# Start of the program

# Function to read an integer and return its absolute value
user_input = abs(int(input()))
index = 0

# Infinite loop to find the relevant triangular number
while True:
    # Calculate the current triangular number
    triangular_number = (index * (index + 1)) / 2
    
    # Calculate the difference from the input
    difference = triangular_number - user_input

    # Check if we have found an exact match
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

# End of the program
