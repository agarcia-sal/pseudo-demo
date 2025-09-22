# Start

# Receive Input
targetValue = abs(int(input()))

# Initialize Counter
index = 0

# Infinite Loop
while True:
    # Calculate Triangle Number
    triangularNumber = (index * (index + 1)) // 2  # Use integer division

    # Calculate Difference
    difference = triangularNumber - targetValue

    # Check Conditions
    if triangularNumber == targetValue:
        print(index)  # Result when triangularNumber equals targetValue
        break  # Exit the loop
    elif triangularNumber > targetValue:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Result when difference is even
            break  # Exit the loop

    # Increment Counter
    index += 1

# End
