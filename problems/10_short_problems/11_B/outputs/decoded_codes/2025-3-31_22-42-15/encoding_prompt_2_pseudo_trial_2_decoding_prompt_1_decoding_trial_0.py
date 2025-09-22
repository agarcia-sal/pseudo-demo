# 1. Start (Implicit in Python)
# 2. Input: Read an integer value from the user and store its absolute value as targetSum.
targetSum = abs(int(input()))

# 3. Initialize: Set a counter index to 0.
index = 0

# 4. Loop: Begin an infinite loop that continues until a break condition is met:
while True:
    # 4a. Calculate: Compute the sum of the first index natural numbers and store it as currentSum.
    currentSum = index * (index + 1) / 2

    # 4b. Calculate Difference: Determine the difference between currentSum and targetSum, and store it as difference.
    difference = currentSum - targetSum

    # 4c. Check for Exact Match: 
    if currentSum == targetSum:
        # 4c(i). Output: Print the value of index.
        print(index)
        # 4c(ii). Terminate Loop: Exit the loop.
        break

    # 4d. Check for Overshoot: 
    if currentSum > targetSum:
        # 4d(i). Check Parity: If the difference is even:
        if difference % 2 == 0:
            # 4d(ii). Output: Print the value of index.
            print(index)
            # 4d(iii). Terminate Loop: Exit the loop.
            break

    # 4e. Increment: Increase the value of index by 1.
    index += 1

# 5. End (Implicit in Python)
