# Step 1: Get Input
t = int(input())

# Step 2: Initialize a Counter
primeCount = 0

# Step 3: Loop Through Each Number
for currentNumber in range(1, t + 1):
    # a. SET divisorCount to 0
    divisorCount = 0
    # b. SET remainingValue to currentNumber
    remainingValue = currentNumber

    # Step 4: Check for Divisibility
    for potentialDivisor in range(2, currentNumber):
        # i. IF remainingValue is divisible by potentialDivisor THEN
        if remainingValue % potentialDivisor == 0:
            # A. Increment divisorCount by 1
            divisorCount += 1
            # B. WHILE remainingValue is divisible by potentialDivisor DO
            while remainingValue % potentialDivisor == 0:
                # I. Divide remainingValue by potentialDivisor
                remainingValue //= potentialDivisor

    # Step 5: Determine if Prime
    # d. IF divisorCount equals 2 THEN
    if divisorCount == 2:
        # i. Increment primeCount by 1
        primeCount += 1

# Step 6: Output Result
print(primeCount)
