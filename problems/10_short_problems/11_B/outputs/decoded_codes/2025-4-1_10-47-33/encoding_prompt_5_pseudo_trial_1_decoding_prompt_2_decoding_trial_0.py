# Start the program

# Read an integer input from the user
userInput = abs(int(input()))

# Initialize a variable index to 0
index = 0

# Create an infinite loop to continue examining integers
while True:
    # Calculate the sum of the first 'index' integers
    sum = (index * (index + 1)) // 2  # Using integer division

    # Calculate a difference value
    difference = sum - userInput

    # Check if the sum equals userInput
    if sum == userInput:
        print(index)  # Print index as the solution
        break  # End the program

    # Otherwise, check if the sum is greater than userInput
    if sum > userInput:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Print index as the solution
            break  # End the program

    # Increment the index by 1 to check the next integer
    index += 1

# End the program
