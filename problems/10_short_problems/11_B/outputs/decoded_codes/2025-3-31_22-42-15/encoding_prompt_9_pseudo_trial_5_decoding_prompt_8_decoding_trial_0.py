# Receive Input
targetSum = int(input())

# Initialize Variables
currentIndex = 0

# Infinite Loop
while True:
    # Calculate the Sum
    currentSum = (currentIndex * (currentIndex + 1)) // 2

    # Calculate the Difference
    surplus = currentSum - targetSum

    # Check for Exact Match
    if currentSum == targetSum:
        print(currentIndex)
        break

    # Check for Surplus Condition
    if currentSum > targetSum:
        if surplus % 2 == 0:
            print(currentIndex)
            break

    # Increment Index
    currentIndex += 1
