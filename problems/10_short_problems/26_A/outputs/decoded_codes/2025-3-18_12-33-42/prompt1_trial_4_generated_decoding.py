# Step 1: Read an integer value t from user input
t = int(input())

# Step 2: Initialize resultCount to 0
resultCount = 0

# Step 3: For each integer currentNumber from 1 to t
for currentNumber in range(1, t + 1):
    # a. Initialize distinctPrimeCount to 0
    distinctPrimeCount = 0
    # b. Set tempNumber to currentNumber
    tempNumber = currentNumber

    # Step 4: For each integer potentialFactor from 2 to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        # a. If tempNumber is divisible by potentialFactor
        if tempNumber % potentialFactor == 0:
            # i. Increment distinctPrimeCount by 1
            distinctPrimeCount += 1
            # ii. While tempNumber is divisible by potentialFactor
            while tempNumber % potentialFactor == 0:
                # Continue dividing tempNumber by potentialFactor
                tempNumber //= potentialFactor

    # Step 5: After checking all possible factors
    # a. If distinctPrimeCount equals 2
    if distinctPrimeCount == 2:
        # Increment resultCount by 1
        resultCount += 1

# Step 6: Output the value of resultCount
print(resultCount)
