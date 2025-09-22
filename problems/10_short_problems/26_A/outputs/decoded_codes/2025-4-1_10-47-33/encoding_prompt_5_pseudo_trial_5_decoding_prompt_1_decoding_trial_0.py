# Start

# Define the Input
totalNumbers = int(input())

# Initialize Count
primeCount = 0

# Iterate Over Each Number
for currentNumber in range(1, totalNumbers + 1):
    divisorCount = 0  # Counts the number of divisors found
    tempNumber = currentNumber  # Used to check for divisibility

    # Check for Divisibility
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1  # Found a divisor
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor  # Factor out the divisor

    # Determine If Prime
    if divisorCount == 2:  # The conditions for prime number
        primeCount += 1  # Confirming that the current number is prime

# Output the Result
print(primeCount)

# End
