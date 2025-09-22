# Step 1: Read the number of test cases
testCaseCount = int(input())

# Step 2: Initialize primeCount to zero
primeCount = 0

# Step 3: Loop through each currentNumber from 1 to testCaseCount
for currentNumber in range(1, testCaseCount + 1):
    # Step 3a: Initialize divisorCount to zero
    divisorCount = 0
    # Set reducedNumber equal to currentNumber
    reducedNumber = currentNumber
    
    # Step 3b: Loop through potentialDivisor from 2 to currentNumber (exclusive)
    for potentialDivisor in range(2, currentNumber):
        # Step 3c: Check if reducedNumber is divisible by potentialDivisor
        if reducedNumber % potentialDivisor == 0:
            # If it is, increment divisorCount
            divisorCount += 1
            # While reducedNumber is still divisible by potentialDivisor, divide it
            while reducedNumber % potentialDivisor == 0:
                reducedNumber //= potentialDivisor
    
    # Step 3d: Check if divisorCount is exactly 2
    if divisorCount == 2:
        # Increment primeCount
        primeCount += 1

# Step 4: Output the total number of primes found
print(primeCount)
