# Start

# Receive Input
targetValue = abs(int(input()))

# Initialize Counter
index = 0

# Infinite Loop
while True:
    # Calculate Triangle Number
    triangularNumber = (index * (index + 1)) // 2
    
    # Calculate Difference
    difference = triangularNumber - targetValue
    
    # Check Conditions
    if triangularNumber == targetValue:
        print(index)
        break
    elif triangularNumber > targetValue:
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment Counter
    index += 1

# End
