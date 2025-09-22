# Receive input from the user
limit = int(input())

# Initialize the counter for semiprime numbers
semiprimeCount = 0

# Iterate over each number from 1 to the specified limit (inclusive)
for currentNumber in range(1, limit + 1):
    factorCount = 0  # Count of unique prime factors
    tempNumber = currentNumber  # Temporary number for factoring
    
    # Check for prime factors starting from 2
    for potentialFactor in range(2, currentNumber):
        if tempNumber % potentialFactor == 0:  # potentialFactor is a divisor
            factorCount += 1  # Found a new prime factor
            # Factor out potentialFactor completely
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor
    
    # Check if the number is a semiprime (exactly 2 unique prime factors)
    if factorCount == 2:
        semiprimeCount += 1  # Increment the semiprime count

# Output the total count of semiprimes found
print(semiprimeCount)
