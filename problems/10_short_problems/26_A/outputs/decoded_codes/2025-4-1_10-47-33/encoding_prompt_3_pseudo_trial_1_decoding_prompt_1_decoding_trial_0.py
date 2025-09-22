# Input
t = int(input())

# Initialize
totalSemiPrimes = 0

# Process Each Number from 1 to t
for currentNumber in range(1, t + 1):
    divisorCount = 0
    tempNumber = currentNumber

    # Find Prime Factors
    for potentialDivisor in range(2, currentNumber):  # Loop through potential divisors
        if tempNumber % potentialDivisor == 0:  # Check for divisibility
            divisorCount += 1  # Increment divisor count
            
            # Divide tempNumber by potentialDivisor while it is divisible
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor  # Integer division

    # Check for Semi-Prime Condition
    if divisorCount == 2:  # Check if there are exactly two distinct prime factors
        totalSemiPrimes += 1  # Increment the total semi-prime count

# Output the Result
print(totalSemiPrimes)
