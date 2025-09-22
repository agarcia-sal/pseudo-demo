# Function to read an integer input and return its absolute value
def read_absolute_integer():
    user_input = int(input())  # Read the integer input from the user
    return abs(user_input)  # Return the absolute value

# Main code execution starts here
userInput = read_absolute_integer()  # Get the absolute value of the user input
index = 0  # Initialize index to 0

# Infinite loop to find the triangular number condition
while True:
    # Calculate the current triangular number
    triangularNumber = (index * (index + 1)) // 2  # Use integer division
    
    # Calculate the difference from the input
    difference = triangularNumber - userInput

    # Check if we have found a match
    if triangularNumber == userInput:
        print(index)  # Output the current index
        break  # Exit the loop

    # Check if the triangular number exceeds the input
    elif triangularNumber > userInput:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Output the current index
            break  # Exit the loop

    # Increment index for the next triangular number calculation
    index += 1  # Increment index by 1
