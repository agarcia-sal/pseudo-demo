# Step 1: Read input
limit = int(input())

# Step 2: Initialize semiprime count
semiprimeCount = 0

# Step 3: Iterate through each number from 1 to limit (inclusive)
for currentNumber in range(1, limit + 1):
    # Initialize prime factor count
    primeFactorCount = 0
    # Temporary variable for factorization
    tempNumber = currentNumber

    # Step 3c: Check for potential factors starting from 2
    for potentialFactor in range(2, currentNumber):  # exclusive on currentNumber
        if tempNumber % potentialFactor == 0:  # Check divisibility
            primeFactorCount += 1  # Found a prime factor
            
            # While tempNumber is divisible by potentialFactor
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor  # Reduce tempNumber
            
    # Step 3d: Check if we found exactly 2 prime factors
    if primeFactorCount == 2:
        semiprimeCount += 1  # Increment semiprime count

# Step 4: Output the semiprime count
print(semiprimeCount)
