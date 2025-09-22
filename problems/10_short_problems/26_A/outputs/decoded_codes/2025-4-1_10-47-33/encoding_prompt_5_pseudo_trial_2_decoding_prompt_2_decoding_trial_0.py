# Step 1: Get Input
t = int(input())

# Step 2: Initialize a Counter
primeCount = 0

# Step 3: Loop Through Each Number
for currentNumber in range(1, t + 1):
    divisorCount = 0
    remainingValue = currentNumber

    # Step 4: Check for Divisibility
    for potentialDivisor in range(2, currentNumber):
        if remainingValue % potentialDivisor == 0:
            divisorCount += 1
            while remainingValue % potentialDivisor == 0:
                remainingValue //= potentialDivisor

    # Step 5: Determine if Prime
    if divisorCount == 2:
        primeCount += 1

# Step 6: Output Result
print(primeCount)
