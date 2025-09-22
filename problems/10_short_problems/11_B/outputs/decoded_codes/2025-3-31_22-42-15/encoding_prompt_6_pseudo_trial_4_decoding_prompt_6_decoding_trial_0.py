# Importing math module to use the abs function for absolute value
import math

# Step 1: Read an integer input and take its absolute value
input_number = abs(int(input()))

# Step 2: Initialize a variable to keep track of the current index
current_index = 0

# Step 3: Infinite loop to iterate over possible triangular numbers
while True:
    # Calculate the triangular number
    triangular_number = (current_index * (current_index + 1)) / 2

    # Determine the difference between the triangular number and the input
    difference = triangular_number - input_number

    # Check if we have found an exact match
    if triangular_number == input_number:
        print(current_index)  # Output the current index
        break  # Exit the loop

    # Check if the triangular number surpasses the input
    elif triangular_number > input_number:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(current_index)  # Output the current index
            break  # Exit the loop

    # Increment the index for the next iteration
    current_index += 1
