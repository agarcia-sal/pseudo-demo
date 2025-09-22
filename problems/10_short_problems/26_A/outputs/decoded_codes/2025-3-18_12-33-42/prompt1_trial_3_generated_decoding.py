# 1. Input
t = int(input())

# 2. Initialize
resultCount = 0

# 3. Loop
for currentNumber in range(1, t + 1):
    # 3.1 Initialize
    factorCount = 0
    # 3.2 Assign
    tempNumber = currentNumber

    # 3.3 Inner Loop
    for potentialFactor in range(2, currentNumber):
        # 3.3.1 Check Divisibility
        if tempNumber % potentialFactor == 0:
            # 3.3.1.1 Increment Count
            factorCount += 1
            # 3.3.1.2 Factor Out
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor

    # 3.4 Check Semi-Prime Condition
    if factorCount == 2:
        # 3.4.1 Update Result
        resultCount += 1

# 4. Output
print(resultCount)
