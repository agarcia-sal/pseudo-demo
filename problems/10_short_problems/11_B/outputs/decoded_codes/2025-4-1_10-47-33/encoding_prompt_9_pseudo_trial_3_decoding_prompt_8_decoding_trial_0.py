# Step 1: Receive Input
targetValue = abs(int(input()))

# Step 2: Initialize Variables
index = 0

# Step 3: Infinite Loop
while True:
    # 1. Calculate Sum
    currentSum = (index * (index + 1)) // 2
    
    # 2. Calculate Difference
    diff = currentSum - targetValue
    
    # 3. Check for Equality
    if currentSum == targetValue:
        print(index)
        break
    
    # 4. Check for Greater Sum
    if currentSum > targetValue:
        if diff % 2 == 0:
            print(index)
            break
    
    # 5. Increment Index
    index += 1
