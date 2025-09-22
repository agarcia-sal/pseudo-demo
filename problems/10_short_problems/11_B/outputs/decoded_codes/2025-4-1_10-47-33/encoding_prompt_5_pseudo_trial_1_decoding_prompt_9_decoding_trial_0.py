# Start the program

# Read an integer input from the user
userInput = abs(int(input()))

# Initialize a variable index to 0 (this will represent the current integer we are examining)
index = 0

# Create an infinite loop to continue examining integers
while True:
    # Calculate the sum of the first 'index' integers
    sum_of_integers = (index * (index + 1)) // 2  # Use integer division for accuracy
    # Calculate a difference value
    difference = sum_of_integers - userInput

    # Check if the sum equals userInput
    if sum_of_integers == userInput:
        print(index)  # Print index as the solution
        break  # End the program

    # Check if the sum is greater than userInput
    elif sum_of_integers > userInput:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print index as the solution
            break  # End the program

    # Increment the index by 1 to check the next integer
    index += 1
