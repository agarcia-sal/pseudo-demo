# Initialize Variables
targetNumber = abs(int(input()))
index = 0

# Start Infinite Loop
while True:
    # Calculate the Sum
    sumToIndex = (index * (index + 1)) // 2
    
    # Calculate the Difference
    difference = sumToIndex - targetNumber
    
    # Check for Exact Match
    if sumToIndex == targetNumber:
        print(index)
        break
    
    # Check for Exceeding Value
    if sumToIndex > targetNumber:
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment Index
    index += 1
