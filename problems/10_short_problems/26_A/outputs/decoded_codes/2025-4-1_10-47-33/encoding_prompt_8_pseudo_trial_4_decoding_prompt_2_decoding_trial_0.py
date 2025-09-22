# Start Program

# Get Input
totalNumbers = int(input())

# Initialize Count
result = 0  # This variable will keep track of how many numbers meet the criteria.

# Iterate Through Numbers
for currentNumber in range(1, totalNumbers + 1):
    primeFactorCount = 0  # To count how many distinct prime factors the current number has
    tempNumber = currentNumber  # Working number

    # Check for Prime Factors
    for potentialFactor in range(2, currentNumber):
        # Check if tempNumber is divisible by potentialFactor
        if tempNumber % potentialFactor == 0:
            primeFactorCount += 1  # Found a new prime factor
            # Remove all occurrences of this factor
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor

    # Evaluate Condition
    if primeFactorCount == 2:
        result += 1  # Found a number that is the product of exactly two primes

# Output the Result
print(result)  # Show how many numbers are products of exactly two prime numbers

# End Program
