# Begin

# Read the total number of integers to process
totalNumbers = int(input())

# Initialize the result counter for prime numbers
primeCount = 0

# Loop through each number from 1 to totalNumbers
for currentNumber in range(1, totalNumbers + 1):
    # Initialize a counter for distinct prime factors
    distinctPrimeFactorsCount = 0
    number = currentNumber

    # Check for prime factors from 2 to currentNumber - 1
    for possiblePrimeFactor in range(2, currentNumber):
        # If possiblePrimeFactor is a divisor of number
        if number % possiblePrimeFactor == 0:
            # Increment the distinct prime factors count
            distinctPrimeFactorsCount += 1
            
            # Divide number by possiblePrimeFactor until it no longer divides evenly
            while number % possiblePrimeFactor == 0:
                number = number // possiblePrimeFactor  # Use floor division to avoid decimals

    # If there are exactly 2 distinct prime factors, count this number as a prime-like number
    if distinctPrimeFactorsCount == 2:
        primeCount += 1

# Output the total count of numbers with exactly 2 distinct prime factors
print(primeCount)

# End
