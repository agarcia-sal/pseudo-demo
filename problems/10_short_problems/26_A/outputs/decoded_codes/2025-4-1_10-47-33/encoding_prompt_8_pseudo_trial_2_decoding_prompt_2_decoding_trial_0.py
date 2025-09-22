# Step 1: Read an integer value called 'limit' from user input.
limit = int(input())

# Step 2: Initialize a variable 'semiprimeCount' to 0 to keep track of the number of semiprime numbers found.
semiprimeCount = 0

# Step 3: For each integer 'currentNumber' starting from 1 up to 'limit' (inclusive):
for currentNumber in range(1, limit + 1):
    # Step 3a: Initialize a variable 'primeFactorCount' to 0 to count the prime factors of 'currentNumber'.
    primeFactorCount = 0
    # Step 3b: Set 'tempNumber' to 'currentNumber' to use for factorization.
    tempNumber = currentNumber

    # Step 3c: For each integer 'potentialFactor' starting from 2 up to 'currentNumber' (exclusive):
    for potentialFactor in range(2, currentNumber):
        # Step 3ci: If 'tempNumber' is divisible by 'potentialFactor':
        if tempNumber % potentialFactor == 0:
            # Increment 'primeFactorCount' by 1.
            primeFactorCount += 1
            
            # Step 3cii: While 'tempNumber' is divisible by 'potentialFactor':
            while tempNumber % potentialFactor == 0:
                # Divide 'tempNumber' by 'potentialFactor'.
                tempNumber //= potentialFactor

    # Step 3d: If 'primeFactorCount' is exactly 2:
    if primeFactorCount == 2:
        # Increment 'semiprimeCount' by 1.
        semiprimeCount += 1

# Step 4: Output the value of 'semiprimeCount'.
print(semiprimeCount)
