# Start the Program
# Capture user input and convert it to a non-negative integer
inputValue = abs(int(input()))

# Initialize a Counter
currentIndex = 0

# Create an Infinite Loop for Calculation
while True:
    # Calculate the Triangular Number
    triangularSum = (currentIndex * (currentIndex + 1)) // 2  # Using integer division

    # Determine the Difference
    difference = triangularSum - inputValue

    # Check for Exact Match
    if triangularSum == inputValue:
        print(currentIndex)  # Output the valid result
        break  # Exit the loop

    # Check for Condition When Triangular Sum Exceeds Input Value
    if triangularSum > inputValue:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentIndex)  # Output the valid result
            break  # Exit the loop

    # Increment the Counter
    currentIndex += 1  # Increase the value of currentIndex by 1
