# Start Program

# Get Input
totalNumbers = int(input())  # Read an integer value from the user

# Initialize Count
result = 0  # This variable will keep track of how many numbers meet the criteria

# Iterate Through Numbers
for currentNumber in range(1, totalNumbers + 1):
    primeFactorCount = 0  # Count of distinct prime factors
    tempNumber = currentNumber  # A temporary variable to work with

    # Check for Prime Factors
    for potentialFactor in range(2, currentNumber):  # Check potential factors
        if tempNumber % potentialFactor == 0:  # If potentialFactor is a divisor
            primeFactorCount += 1  # Found a new prime factor
            
            # Remove all occurrences of the prime factor
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor

    # Evaluate Condition
    if primeFactorCount == 2:  # If exactly two distinct prime factors found
        result += 1  # Increment result count

# Output the Result
print(result)  # Display the count of numbers that are products of exactly two primes

# End Program
