# Step 1: Initialize Variables
absoluteValue = abs(int(input()))  # Read input and convert to absolute integer
index = 0  # This will be used to calculate triangular numbers

# Step 2: Start an Infinite Loop
while True:
    # Step 1: Calculate Triangular Number
    triangularNumber = (index * (index + 1)) // 2  # Using integer division
    
    # Step 2: Calculate Difference
    difference = triangularNumber - absoluteValue
    
    # Step 3: Check for Equality
    if triangularNumber == absoluteValue:
        print(index)  # Output index
        break  # Exit loop
    
    # Step 4: Check for Greater Value
    if triangularNumber > absoluteValue:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Output index
            break  # Exit loop
    
    # Step 5: Increment Index
    index += 1
