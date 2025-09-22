# Step 1: Read an integer input value `t`
t = int(input())

# Step 2: Initialize a variable `resultCount` to 0
resultCount = 0

# Step 3: Loop for each number `currentNumber` from 1 to `t`
for currentNumber in range(1, t + 1):
    # Initialize count of distinct prime factors
    distinctPrimeFactorsCount = 0
    tempNumber = currentNumber  # Start the tempNumber with currentNumber

    # Loop for each integer `potentialFactor` starting from 2
    for potentialFactor in range(2, currentNumber):
        # Check if tempNumber is divisible by potentialFactor
        if tempNumber % potentialFactor == 0:
            # Increment distinct prime factors count
            distinctPrimeFactorsCount += 1
            
            # Eliminate all occurrences of this factor
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor

    # Check if distinctPrimeFactorsCount equals 2
    if distinctPrimeFactorsCount == 2:
        # Increment result count
        resultCount += 1

# Step 4: Output the value of resultCount
print(resultCount)
