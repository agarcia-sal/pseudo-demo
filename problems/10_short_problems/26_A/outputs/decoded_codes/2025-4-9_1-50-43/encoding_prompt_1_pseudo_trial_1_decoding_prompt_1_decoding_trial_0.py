# Start Program

# Input the limit
totalNumbers = int(input())

# Initialize the composite count
compositeCount = 0

# Loop through each number from 1 to the limit
for currentNumber in range(1, totalNumbers + 1):
    
    # Initialize factor count
    distinctPrimeFactorCount = 0
    numberToCheck = currentNumber
    
    # Check for factors
    for potentialFactor in range(2, currentNumber):
        if numberToCheck % potentialFactor == 0:
            distinctPrimeFactorCount += 1
            # While numberToCheck is divisible by potentialFactor
            while numberToCheck % potentialFactor == 0:
                numberToCheck //= potentialFactor  # Reduce numberToCheck
    
    # Check for two distinct prime factors
    if distinctPrimeFactorCount == 2:
        compositeCount += 1

# Output the result
print(compositeCount)
