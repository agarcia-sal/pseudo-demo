# Initialize Variables
absoluteValue = abs(int(input()))
index = 0  # This will be used to calculate triangular numbers

# Start an Infinite Loop
while True:
    # Calculate Triangular Number
    triangularNumber = (index * (index + 1)) // 2
    
    # Calculate Difference
    difference = triangularNumber - absoluteValue
    
    # Check for Equality
    if triangularNumber == absoluteValue:
        print(index)
        break
    
    # Check for Greater Value
    if triangularNumber > absoluteValue:
        if difference % 2 == 0:
            print(index)
            break
    
    # Increment Index
    index += 1
