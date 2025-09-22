# BEGIN

# Read the input value indicating how many numbers to check
totalNumbers = int(input())

# Initialize a counter for numbers with exactly two distinct prime factors
primeFactorCount = 0

# Loop through each number from 1 to totalNumbers
for number in range(1, totalNumbers + 1):
    # Initialize a count for distinct prime factors found in the current number
    factorCount = 0
    currentNumber = number
    
    # Set to keep track of distinct prime factors
    distinctPrimes = set()
    
    # Check for factors from 2 up to the square root of the current number (inclusive)
    for factor in range(2, int(currentNumber**0.5) + 1):
        # If the factor divides the current number
        if currentNumber % factor == 0:
            # Increment the count of found prime factors
            distinctPrimes.add(factor)
            
            # Divide the current number by the factor until it no longer divides evenly
            while currentNumber % factor == 0:
                currentNumber //= factor
    
    # If there is a remainder greater than 1, then it is a prime factor itself
    if currentNumber > 1:
        distinctPrimes.add(currentNumber)

    # If exactly two distinct prime factors were found
    if len(distinctPrimes) == 2:
        # Increment the total count of such numbers
        primeFactorCount += 1

# Output the total count of numbers with exactly two distinct prime factors
print(primeFactorCount)

# END
