# 1. Input Step
targetSum = abs(int(input()))

# 2. Initialization Step
index = 0

# 3. Looping Step
while True:
    # Calculate the triangular number
    sumUpToIndex = (index * (index + 1)) // 2  # Use integer division

    # Calculate the difference
    excessAmount = sumUpToIndex - targetSum

    # Condition Check
    if sumUpToIndex == targetSum:
        print(index)
        break

    if sumUpToIndex > targetSum:
        if excessAmount % 2 == 0:  # Check if excessAmount is even
            print(index)
            break

    # Increment Step
    index += 1
