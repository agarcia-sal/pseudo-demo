# 1. Initialize Variables
absoluteValue = abs(int(input()))
index = 0  # Starting point for triangular numbers

# 2. Start an Infinite Loop
while True:
    # 1. Calculate Triangular Number
    triangularNumber = (index * (index + 1)) // 2  # Using integer division
    
    # 2. Calculate Difference
    difference = triangularNumber - absoluteValue
    
    # 3. Check for Equality
    if triangularNumber == absoluteValue:
        print(index)  # Output index
        break  # Exit the loop
    
    # 4. Check for Greater Value
    if triangularNumber > absoluteValue:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Output index
            break  # Exit the loop
    
    # 5. Increment Index
    index += 1
