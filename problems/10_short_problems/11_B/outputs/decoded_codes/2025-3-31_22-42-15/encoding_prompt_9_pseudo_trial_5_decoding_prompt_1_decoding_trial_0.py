# Step 1: Receive Input
targetSum = int(input())

# Step 2: Initialize Variables
currentIndex = 0

# Step 3: Infinite Loop
while True:
    # Step 3.1: Calculate the Sum
    currentSum = (currentIndex * (currentIndex + 1)) / 2
    
    # Step 3.2: Calculate the Difference
    surplus = currentSum - targetSum
    
    # Step 3.3: Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)
        break
    
    # Step 3.4: Check for Surplus Condition
    if currentSum > targetSum:
        if surplus % 2 == 0:
            print(currentIndex)
            break
    
    # Step 3.5: Increment Index
    currentIndex += 1
