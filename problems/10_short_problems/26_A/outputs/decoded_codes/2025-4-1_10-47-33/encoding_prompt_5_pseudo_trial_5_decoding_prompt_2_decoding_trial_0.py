# Start

# Define the Input
totalNumbers = int(input())  # Read an integer value as the upper limit of the range

# Initialize Count
primeCount = 0  # This will keep track of the number of prime numbers found

# Iterate Over Each Number
for currentNumber in range(1, totalNumbers + 1):  # From 1 to totalNumbers inclusive
    divisorCount = 0  # Count the number of divisors for the current number
    tempNumber = currentNumber  # Use this number to check for divisibility

    # Check for Divisibility
    for potentialDivisor in range(2, currentNumber):  # From 2 to currentNumber - 1
        if tempNumber % potentialDivisor == 0:  # Check if divisible
            divisorCount += 1  # Found a divisor
            while tempNumber % potentialDivisor == 0:  # Factor out the divisor completely
                tempNumber //= potentialDivisor  # Reduce the number

    # Determine If Prime
    if divisorCount == 1:  # Check if there is only one divisor (the number itself)
        primeCount += 1  # It is a prime number

# Output the Result
print(primeCount)  # Print the total number of prime numbers up to totalNumbers

# End
