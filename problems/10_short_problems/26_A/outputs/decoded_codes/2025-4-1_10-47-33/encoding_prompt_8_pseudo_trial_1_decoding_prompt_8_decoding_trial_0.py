# Start the Program
totalCount = int(input())

# Initialize a Result Variable
countOfNumbersWithTwoDistinctPrimeFactors = 0

# Loop Through Each Number
for currentNumber in range(1, totalCount + 1):
    distinctPrimeFactorsCount = 0
    workingNumber = currentNumber

    # Check for Prime Factors
    for potentialFactor in range(2, currentNumber):
        if workingNumber % potentialFactor == 0:
            distinctPrimeFactorsCount += 1
            while workingNumber % potentialFactor == 0:
                workingNumber //= potentialFactor

    # Check for Two Distinct Factors
    if distinctPrimeFactorsCount == 2:
        countOfNumbersWithTwoDistinctPrimeFactors += 1

# Output the Result
print(countOfNumbersWithTwoDistinctPrimeFactors)
