# Read the total number of test cases
totalTestCases = int(input())

# Initialize the result counter for prime numbers
primeCount = 0

# Loop through each number from 1 to totalTestCases
for currentNumber in range(1, totalTestCases + 1):
    
    # Initialize a counter for the number of distinct prime factors
    distinctPrimeFactors = 0
    
    # Copy the current number to a variable for factorization
    factorableNumber = currentNumber
    
    # Check for factors starting from 2 up to the current number
    for potentialFactor in range(2, currentNumber):
        
        # Check if potentialFactor is a divisor of factorableNumber
        if factorableNumber % potentialFactor == 0:
            
            # Increment the distinct prime factors counter
            distinctPrimeFactors += 1
            
            # Divide factorableNumber by potentialFactor until it no longer divides evenly
            while factorableNumber % potentialFactor == 0:
                factorableNumber //= potentialFactor
            
    # Check if the number has exactly two distinct prime factors
    if distinctPrimeFactors == 2:
        # Increment the primeCount for each valid currentNumber
        primeCount += 1

# Display the total count of numbers with exactly two distinct prime factors
print(primeCount)
