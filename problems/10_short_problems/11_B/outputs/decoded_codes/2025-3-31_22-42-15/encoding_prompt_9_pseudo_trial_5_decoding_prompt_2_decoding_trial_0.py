# 1. Receive Input
targetSum = int(input())

# 2. Initialize Variables
currentIndex = 0

# 3. Infinite Loop
while True:
    # 1. Calculate the Sum
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Using integer division

    # 2. Calculate the Difference
    surplus = currentSum - targetSum

    # 3. Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)
        break  # Exit the loop
        
    # 4. Check for Surplus Condition
    if currentSum > targetSum:
        if surplus % 2 == 0:
            print(currentIndex)
            break  # Exit the loop
            
    # 5. Increment Index
    currentIndex += 1
