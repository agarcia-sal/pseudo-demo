# Start the Program
totalCount = int(input())  # Read an integer value from the user

# Initialize the result variable
countOfNumbersWithTwoDistinctPrimeFactors = 0  # Count of numbers with two distinct prime factors

# Loop through each number from 1 to totalCount (inclusive)
for currentNumber in range(1, totalCount + 1):
    distinctPrimeFactorsCount = 0  # Track how many distinct prime factors currentNumber has
    workingNumber = currentNumber  # Store original value of currentNumber

    # Check for prime factors
    for potentialFactor in range(2, currentNumber):  # Check potential factors from 2 up to (but not including) currentNumber
        if workingNumber % potentialFactor == 0:  # Check if workingNumber is divisible by potentialFactor
            distinctPrimeFactorsCount += 1  # Increment the count of distinct prime factors
            # While workingNumber is divisible by potentialFactor, divide it
            while workingNumber % potentialFactor == 0:
                workingNumber //= potentialFactor  # Remove all occurrences of this prime factor

    # Check for two distinct prime factors
    if distinctPrimeFactorsCount == 2:  # Exactly two distinct prime factors found
        countOfNumbersWithTwoDistinctPrimeFactors += 1  # Increment the count

# Output the result
print(countOfNumbersWithTwoDistinctPrimeFactors)  # Print final count of numbers with two distinct prime factors
