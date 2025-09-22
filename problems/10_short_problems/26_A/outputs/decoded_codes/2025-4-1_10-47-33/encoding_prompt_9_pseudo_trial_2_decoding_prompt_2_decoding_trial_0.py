# 1. Get User Input
maximumNumber = int(input())

# 2. Initialize Count of Prime Numbers
primeCount = 0

# 3. Loop Through Each Number
for currentNumber in range(1, maximumNumber + 1):
    factorCount = 0
    remainingNumber = currentNumber
    
    # 4. Check for Factors
    for potentialFactor in range(2, currentNumber):
        if remainingNumber % potentialFactor == 0:
            factorCount += 1
            # Remove the factor
            while remainingNumber % potentialFactor == 0:
                remainingNumber //= potentialFactor
                
    # 5. Identify Prime Number
    if factorCount == 1:  # Since we're starting count at 1, we check for one factor only (itself)
        primeCount += 1

# 6. Output the Result
print(primeCount)
