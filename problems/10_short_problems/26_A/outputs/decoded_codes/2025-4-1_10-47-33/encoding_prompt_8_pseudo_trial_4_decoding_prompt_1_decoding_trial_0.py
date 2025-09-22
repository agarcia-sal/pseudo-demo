# 1. Start Program

# 2. Get Input
totalNumbers = int(input())

# 3. Initialize Count
result = 0  # This variable will keep track of how many numbers meet the criteria.

# 4. Iterate Through Numbers
for currentNumber in range(1, totalNumbers + 1):
    primeFactorCount = 0  # a. Initialize a variable primeFactorCount to count distinct prime factors.
    tempNumber = currentNumber  # b. Set tempNumber to currentNumber to work with.

    # 5. Check for Prime Factors
    for potentialFactor in range(2, currentNumber):  # a. For each potential factor.
        if tempNumber % potentialFactor == 0:  # Check if tempNumber is divisible by potentialFactor.
            primeFactorCount += 1  # i. Increment primeFactorCount by 1.
            # ii. While tempNumber is divisible by potentialFactor, remove all occurrences.
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor  # Remove the factor.

    # 6. Evaluate Condition
    if primeFactorCount == 2:  # Check if we found exactly two distinct prime factors.
        result += 1  # Increment result.

# 7. Output the Result
print(result)  # Print the number of products of exactly two prime numbers.

# 8. End Program
