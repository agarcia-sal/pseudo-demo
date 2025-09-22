# Receive Input
targetNumber = abs(int(input()))

# Initialize Variables
integerIndex = 0

# Start Loop
while True:
    # Calculate Triangular Number
    triangularNumber = (integerIndex * (integerIndex + 1)) / 2

    # Calculate Difference
    difference = triangularNumber - targetNumber

    # Check Conditions
    if triangularNumber == targetNumber:
        print(integerIndex)
        break
    elif triangularNumber > targetNumber:
        if difference % 2 == 0:
            print(integerIndex)
            break

    # Increment Index
    integerIndex += 1
