# Start of the program

# Get User Input
input_number = int(input())  # Read a number from the user as a positive integer

# Initialize a Counter
current_number = 0

# Begin an Infinite Loop
while True:
    # Calculate the Triangular Number
    triangular_number = (current_number * (current_number + 1)) // 2

    # Calculate the Difference
    difference = triangular_number - input_number

    # Check for Equality
    if triangular_number == input_number:
        print(current_number)  # Print the current number
        break  # Exit the loop

    # Check for Greater Value
    elif triangular_number > input_number:
        # If difference is even
        if difference % 2 == 0:
            print(current_number)  # Print the current number
            break  # Exit the loop

    # Increment the Counter
    current_number += 1  # Increase current_number by 1

# End of the program
