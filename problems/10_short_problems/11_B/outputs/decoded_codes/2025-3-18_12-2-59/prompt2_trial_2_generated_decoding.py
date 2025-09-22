# Input Phase
targetNumber = int(input())  # Get user input for the number
targetNumber = abs(targetNumber)  # Calculate the absolute value

# Initialization
index = 0  # Initialize a counter variable

# Loop Phase
while True:  # Begin an infinite loop
    # Calculate the sum of integers from 0 to index
    sumOfIntegers = (index * (index + 1)) // 2  # Using the formula for the sum of first n integers

    # Calculate the difference
    difference = sumOfIntegers - targetNumber  # Calculate the difference

    # Check if sumOfIntegers equals targetNumber
    if sumOfIntegers == targetNumber:
        print(index)  # Display index
        break  # Exit the loop

    # Check if sumOfIntegers is greater than targetNumber
    if sumOfIntegers > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(index)  # Display index
            break  # Exit the loop

    # Increment index by 1 to continue checking the next integer
    index += 1
