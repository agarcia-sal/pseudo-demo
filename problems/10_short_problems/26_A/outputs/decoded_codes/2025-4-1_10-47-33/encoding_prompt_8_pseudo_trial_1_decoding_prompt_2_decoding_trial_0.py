# Step 1: Start the Program
totalCount = int(input())

# Step 2: Initialize a Result Variable
countOfNumbersWithTwoDistinctPrimeFactors = 0

# Step 3: Loop Through Each Number
for currentNumber in range(1, totalCount + 1):
    distinctPrimeFactorsCount = 0  # Reset the count for this number
    workingNumber = currentNumber   # Store the original number for manipulation

    # Step 3.1: Check for Prime Factors
    for potentialFactor in range(2, currentNumber):
        if workingNumber % potentialFactor == 0:  # Check if divisible
            distinctPrimeFactorsCount += 1  # Found a new prime factor
            # Remove all occurrences of this prime factor from workingNumber
            while workingNumber % potentialFactor == 0:
                workingNumber //= potentialFactor

    # Step 3.2: Check for Two Distinct Factors
    if distinctPrimeFactorsCount == 2:
        countOfNumbersWithTwoDistinctPrimeFactors += 1

# Step 4: Output the Result
print(countOfNumbersWithTwoDistinctPrimeFactors)
