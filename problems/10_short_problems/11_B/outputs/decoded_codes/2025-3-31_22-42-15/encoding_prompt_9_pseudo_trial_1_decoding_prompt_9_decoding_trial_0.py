# Initialize Variables
absoluteValue = abs(int(input()))  # Convert input to integer and take absolute value
index = 0  # This will be used to calculate triangular numbers

# Start an Infinite Loop
while True:
    # Calculate Triangular Number
    triangularNumber = (index * (index + 1)) // 2  # Using integer division for triangular number

    # Calculate Difference
    difference = triangularNumber - absoluteValue

    # Check for Equality
    if triangularNumber == absoluteValue:
        print(index)  # Output index if triangular number matches absolute value
        break  # Exit the loop

    # Check for Greater Value
    if triangularNumber > absoluteValue:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Output index if difference is even
            break  # Exit the loop

    # Increment Index
    index += 1  # Increase index by 1
