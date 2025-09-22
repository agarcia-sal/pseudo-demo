# BEGIN

# Read an integer input, take its absolute value
inputNumber = abs(int(input()))

# Initialize a variable to keep track of the current index
currentIndex = 0

# Infinite loop to iterate over possible triangular numbers
while True:

    # Calculate the sum of the first currentIndex natural numbers (triangular number)
    triangularNumber = (currentIndex * (currentIndex + 1)) / 2

    # Determine the difference between the triangular number and the input
    difference = triangularNumber - inputNumber

    # Check if we have found an exact match
    if triangularNumber == inputNumber:
        print(currentIndex)  # Output the current index
        break  # Exit the loop

    # Check if the triangular number surpasses the input
    elif triangularNumber > inputNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(currentIndex)  # Output the current index
            break  # Exit the loop

    # Increment the index for the next iteration
    currentIndex += 1

# END
