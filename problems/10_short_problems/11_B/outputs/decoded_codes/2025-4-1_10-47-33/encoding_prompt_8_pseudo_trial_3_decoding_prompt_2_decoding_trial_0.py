# Initialize Variables
targetNumber = abs(int(input()))  # Get the absolute value of the input number
index = 0  # Set index variable to 0

# Start Infinite Loop
while True:
    # Calculate the Sum
    sumToIndex = (index * (index + 1)) // 2  # Use integer division to calculate the sum up to index

    # Calculate the Difference
    difference = sumToIndex - targetNumber

    # Check for Exact Match
    if sumToIndex == targetNumber:
        print(index)  # Print the current index
        break  # Exit the loop

    # Check for Exceeding Value
    if sumToIndex > targetNumber:
        if difference % 2 == 0:  # Check if the difference is even
            print(index)  # Print the current index
            break  # Exit the loop

    # Increment Index
    index += 1  # Increase index by 1
