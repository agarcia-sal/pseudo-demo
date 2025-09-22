# Step 1: Start

# Step 2: Receive Input
targetValue = abs(int(input()))

# Step 3: Initialize Counter
index = 0

# Step 4: Infinite Loop
while True:
    # Step 4a: Calculate Triangle Number
    triangularNumber = (index * (index + 1)) // 2  # Using integer division
    
    # Step 4b: Calculate Difference
    difference = triangularNumber - targetValue
    
    # Step 4c: Check Conditions
    if triangularNumber == targetValue:
        print(index)  # Print result
        break  # Exit the loop
    elif triangularNumber > targetValue:
        if difference % 2 == 0:  # Check if difference is even
            print(index)  # Print result
            break  # Exit the loop
    
    # Step 4d: Increment Counter
    index += 1

# Step 5: End
