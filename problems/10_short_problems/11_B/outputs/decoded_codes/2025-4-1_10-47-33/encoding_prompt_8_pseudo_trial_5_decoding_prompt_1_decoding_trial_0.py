# Start the Program
inputValue = abs(int(input()))  # Capture user input and convert it to a non-negative integer

# Initialize a Counter
currentIndex = 0

# Create an Infinite Loop for Calculation
while True:
    # Calculate the Triangular Number
    triangularSum = (currentIndex * (currentIndex + 1)) // 2  # Calculate triangular number

    # Determine the Difference
    difference = triangularSum - inputValue  # Calculate the difference

    # Check for Exact Match
    if triangularSum == inputValue:
        print(currentIndex)  # Output the currentIndex
        break  # Exit the loop

    # Check for Condition When Triangular Sum Exceeds Input Value
    if triangularSum > inputValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentIndex)  # Output the currentIndex
            break  # Exit the loop

    # Increment the Counter
    currentIndex += 1  # Increase currentIndex by 1

# End the Program
