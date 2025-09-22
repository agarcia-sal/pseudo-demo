# Start the program

# Read an integer input from the user and take its absolute value
user_input = abs(int(input()))

# Initialize a variable to represent the current integer we are examining
current_index = 0

# Create an infinite loop to continue examining integers
while True:
    # Calculate the sum of the first 'current_index' integers using the formula
    sum_of_integers = (current_index * (current_index + 1)) // 2

    # Calculate the difference value
    difference = sum_of_integers - user_input

    # Check if the sum equals user_input
    if sum_of_integers == user_input:
        print(current_index)  # Print the solution
        break  # End the program

    # Check if the sum is greater than user_input
    elif sum_of_integers > user_input:
        # Check if the difference is even
        if difference % 2 == 0:
            print(current_index)  # Print the solution
            break  # End the program

    # Increment the index by 1 to check the next integer
    current_index += 1
