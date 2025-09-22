# Get an integer input from the user and convert it to absolute value
absolute_input = abs(int(input()))

# Initialize the counter variable for the current integer
current_integer = 0

# Loop indefinitely to find the correct triangular number
while True:
    # Calculate the triangular number for the current integer
    triangular_number = (current_integer * (current_integer + 1)) // 2  # Using integer division

    # Calculate the difference between the triangular number and the absolute input
    difference = triangular_number - absolute_input

    # Check if the triangular number exactly equals the absolute input
    if triangular_number == absolute_input:
        print(current_integer)  # Output the current integer
        break  # Exit the loop
        
    # Check if the triangular number exceeds the absolute input
    elif triangular_number > absolute_input:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_integer)  # Output the current integer
            break  # Exit the loop

    # Increment the current integer for the next iteration
    current_integer += 1
