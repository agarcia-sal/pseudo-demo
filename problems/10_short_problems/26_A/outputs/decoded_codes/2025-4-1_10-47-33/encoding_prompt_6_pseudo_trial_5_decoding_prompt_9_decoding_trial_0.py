# Read an integer from the user
t = int(input())

# Initialize the count of numbers with exactly two distinct prime factors
totalCount = 0

# Loop through each number from 1 to t
for currentNumber in range(1, t + 1):
    distinctPrimeCount = 0  # Track distinct prime factors
    currentValue = currentNumber  # Start factorizing currentNumber

    # Find prime factors
    for potentialPrime in range(2, currentNumber):  # Check potential prime factors
        if currentValue % potentialPrime == 0:  # Check if potentialPrime divides currentValue
            distinctPrimeCount += 1  # Found a new distinct prime factor
            
            # Divide currentValue by potentialPrime until it's no longer divisible
            while currentValue % potentialPrime == 0:
                currentValue //= potentialPrime  # Breaking down currentNumber

    # Check if the count of distinct prime factors is exactly two
    if distinctPrimeCount == 2:
        totalCount += 1  # Increment the total count

# Output the result: number of integers with exactly two distinct prime factors
print(totalCount)
