# Start Program

# Get Input
totalNumbers = int(input())

# Initialize Result
countOfNumbersWithTwoPrimeFactors = 0

# Loop Through Each Number
for currentNumber in range(1, totalNumbers + 1):
    # Initialize Prime Factor Count
    distinctPrimeFactorCount = 0
    number = currentNumber
    
    # Check for Prime Factors
    for possibleFactor in range(2, currentNumber):
        if number % possibleFactor == 0:  # If number is divisible by possibleFactor
            distinctPrimeFactorCount += 1  # Increment the count of distinct prime factors
            
            # While number is divisible by possibleFactor
            while number % possibleFactor == 0:
                number //= possibleFactor  # Reduce number by possibleFactor
                
    # Evaluate Count of Distinct Prime Factors
    if distinctPrimeFactorCount == 2:
        countOfNumbersWithTwoPrimeFactors += 1  # Increment the count

# Output Result
print(countOfNumbersWithTwoPrimeFactors)

# End Program
