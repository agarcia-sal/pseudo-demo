# Step 1: Receive an integer input
totalNumbers = int(input())

# Step 2: Initialize primeCount to 0
primeCount = 0

# Step 3: Loop over each integer from 1 to totalNumbers (inclusive)
for currentNumber in range(1, totalNumbers + 1):
    # Set a counter for distinct divisors
    divisorCount = 0
    numerator = currentNumber

    # Step 4: Loop for potentialDivisor from 2 to currentNumber (exclusive)
    for potentialDivisor in range(2, currentNumber):
        # Check if numerator is divisible by potentialDivisor
        if numerator % potentialDivisor == 0:
            divisorCount += 1  # Increment divisorCount
            # While numerator is divisible by potentialDivisor
            while numerator % potentialDivisor == 0:
                numerator //= potentialDivisor  # Remove factors of potentialDivisor

    # Step 5: Check if divisorCount equals 2
    if divisorCount == 2:
        primeCount += 1  # Increment primeCount

# Step 6: Output the total number of prime numbers found
print(primeCount)
