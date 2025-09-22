# Start Program

# Get the Input
total = int(input())

# Initialize Count of Prime Numbers
primeCount = 0

# Iterate Through Possible Numbers
for currentNumber in range(1, total + 1):
    divisorCount = 0  # Count of divisors
    workingNum = currentNumber  # Number to check for primality
    
    # Check for Divisibility
    for potentialDivisor in range(2, currentNumber):
        if workingNum % potentialDivisor == 0:
            divisorCount += 1
            while workingNum % potentialDivisor == 0:
                workingNum //= potentialDivisor
        
    # Determine if Prime
    if divisorCount == 2:
        primeCount += 1  # Increment prime count

# Output Result
print(primeCount)

# End Program
