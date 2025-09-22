# Step 1: Receive Input
targetValue = abs(int(input()))

# Step 2: Initialize Variables
index = 0

# Step 3: Infinite Loop
while True:
    # Step 1: Calculate Sum
    currentSum = (index * (index + 1)) / 2
    
    # Step 2: Calculate Difference
    diff = currentSum - targetValue
    
    # Step 3: Check for Equality
    if currentSum == targetValue:
        print(index)
        break
    
    # Step 4: Check for Greater Sum
    if currentSum > targetValue:
        if diff % 2 == 0:  # Check if diff is even
            print(index)
            break
    
    # Step 5: Increment Index
    index += 1
