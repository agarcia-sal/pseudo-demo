# BEGIN

# Read the number of test cases
numberOfTests = int(input())

# Initialize the result counter for prime numbers
primeCount = 0

# Iterate through each number from 1 to numberOfTests
for number in range(1, numberOfTests + 1):

    # Initialize a counter for the number of distinct prime factors
    distinctPrimeFactorCount = 0
    
    # Make a copy of the current number to factorize
    currentNumber = number
    
    # Check for potential prime factors from 2 up to (but not including) the current number
    for factor in range(2, number):

        # If the current number is divisible by the factor
        if currentNumber % factor == 0:
            # Increment the distinct prime factor counter
            distinctPrimeFactorCount += 1
            
            # Divide the current number by the factor until it's no longer divisible
            while currentNumber % factor == 0:
                currentNumber //= factor

    # If the number has exactly two distinct prime factors, consider it a valid result
    if distinctPrimeFactorCount == 2:
        primeCount += 1

# Output the total count of numbers with exactly two distinct prime factors
print(primeCount)

# END
