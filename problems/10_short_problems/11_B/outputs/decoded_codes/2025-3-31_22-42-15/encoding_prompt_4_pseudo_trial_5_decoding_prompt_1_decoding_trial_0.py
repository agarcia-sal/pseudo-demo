# Read an integer input from the user and take its absolute value
userInput = abs(int(input()))
index = 0

# Infinite loop to find the triangular number condition
while True:
    # Calculate the current triangular number
    triangularNumber = (index * (index + 1)) // 2
    
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
    index += 1
