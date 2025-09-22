# 1. Start

# 2. Input: Read an integer from the user and store the absolute value in a variable named `targetSum`.
targetSum = abs(int(input()))

# 3. Initialize: Set a variable `currentIndex` to 0.
currentIndex = 0

# 4. Loop: Begin an infinite loop that will continue until explicitly broken.
while True:
    # 4.1. Calculate: Determine the sum of the first `currentIndex` integers.
    currentSum = (currentIndex * (currentIndex + 1)) // 2

    # 4.2. Calculate Difference: Find the difference between `currentSum` and `targetSum`.
    differenceFromTarget = currentSum - targetSum

    # 4.3. Check for Exact Match: If `currentSum` is equal to `targetSum`.
    if currentSum == targetSum:
        # Output the value of `currentIndex`.
        print(currentIndex)
        break  # Exit the loop.

    # 4.4. Check for Exceeding Target: If `currentSum` is greater than `targetSum`.
    if currentSum > targetSum:
        # Check if `differenceFromTarget` is even.
        if differenceFromTarget % 2 == 0:
            # Output the value of `currentIndex`.
            print(currentIndex)
            break  # Exit the loop.

    # 4.5. Increment: Increase `currentIndex` by 1.
    currentIndex += 1

# 6. End
