# Start the program

# Read an integer input from the user
user_input = abs(int(input()))  # Set the variable userInput to the absolute value of the input integer

# Initialize a variable index to 0 (this will represent the current integer we are examining)
index = 0

# Create an infinite loop to continue examining integers
while True:
    # Calculate the sum of the first 'index' integers
    total_sum = (index * (index + 1)) // 2  # Using integer division for exact integer result

    # Calculate a difference value
    difference = total_sum - user_input

    # Check if the sum equals userInput
    if total_sum == user_input:
        print(index)  # Print index as the solution
        break  # End the program

    # Otherwise, check if the sum is greater than userInput
    if total_sum > user_input:
        # Check if the difference is even
        if difference % 2 == 0:  # If the difference is even
            print(index)  # Print index as the solution
            break  # End the program

    # Increment the index by 1 to check the next integer
    index += 1
