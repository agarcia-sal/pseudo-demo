# Get User Input
maximumNumber = int(input())

# Initialize Count of Prime Numbers
primeCount = 0

# Loop Through Each Number
for currentNumber in range(1, maximumNumber + 1):
    factorCount = 0
    remainingNumber = currentNumber

    # Check for Factors
    for potentialFactor in range(2, currentNumber):
        if remainingNumber % potentialFactor == 0:
            factorCount += 1
            while remainingNumber % potentialFactor == 0:
                remainingNumber //= potentialFactor

    # Identify Prime Number
    if factorCount == 1 and currentNumber > 1:  # Adjusted condition to identify prime numbers correctly
        primeCount += 1

# Output the Result
print(primeCount)
