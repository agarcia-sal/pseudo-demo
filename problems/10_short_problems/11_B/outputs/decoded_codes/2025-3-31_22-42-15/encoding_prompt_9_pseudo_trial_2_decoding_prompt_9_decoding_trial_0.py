# Receive Input
targetNumber = abs(int(input()))

# Initialize Variables
currentInteger = 0

# Start an Infinite Loop
while True:
    # Calculate Triangular Number
    triangularNumber = (currentInteger * (currentInteger + 1)) // 2
    
    # Determine the Difference
    difference = triangularNumber - targetNumber
    
    # Check Conditions
    if triangularNumber == targetNumber:
        print(currentInteger)  # Output currentInteger
        break  # Exit the loop (valid number found)
    
    elif triangularNumber > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(currentInteger)  # Output currentInteger
            break  # Exit the loop (valid adjustment found)
    
    # Increment the Integer
    currentInteger += 1
