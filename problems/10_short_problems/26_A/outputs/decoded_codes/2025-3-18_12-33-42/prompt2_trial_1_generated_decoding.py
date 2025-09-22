# Step 1: Read an integer value from the user and store it as totalCount
totalCount = int(input())

# Step 2: Initialize a counter called primeCount to zero
primeCount = 0

# Step 3: For each integer currentNumber starting from 1 to totalCount
for currentNumber in range(1, totalCount + 1):
    # Initialize a counter called divisorCount to zero
    divisorCount = 0
    # Set a temporary variable temporaryNumber equal to currentNumber
    temporaryNumber = currentNumber

    # Step 4: For each integer potentialDivisor starting from 2 to currentNumber - 1
    for potentialDivisor in range(2, currentNumber):
        # Check if temporaryNumber can be divided evenly by potentialDivisor
        if temporaryNumber % potentialDivisor == 0:
            # Increment divisorCount by one
            divisorCount += 1
            # Step 4.2: While temporaryNumber is divisible by potentialDivisor
            while temporaryNumber % potentialDivisor == 0:
                # Divide temporaryNumber by potentialDivisor
                temporaryNumber //= potentialDivisor
    
    # Step 5: Determine if exactly two distinct divisors were found
    if divisorCount == 2:
        # Increment primeCount by one
        primeCount += 1

# Step 6: Output the final value of primeCount
print(primeCount)
