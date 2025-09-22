# Read input for the upper limit to check for semi-prime numbers
t = int(input())

# Initialize the count of semi-prime numbers
totalSemiPrimes = 0

# Process each number from 1 to t
for currentNumber in range(1, t + 1):
    divisorCount = 0
    tempNumber = currentNumber
    
    # Find prime factors
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1
            
            # While tempNumber is divisible by potentialDivisor
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor

    # Check for semi-prime condition
    if divisorCount == 2:
        totalSemiPrimes += 1

# Output the result
print(totalSemiPrimes)
