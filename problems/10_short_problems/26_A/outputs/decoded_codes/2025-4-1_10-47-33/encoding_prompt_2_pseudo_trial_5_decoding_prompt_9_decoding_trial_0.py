# Get the total number of integers to check for primality
totalNumbers = int(input())

# Initialize a counter for prime numbers
primeCount = 0

# Loop through each integer from 1 to totalNumbers
for currentNumber in range(1, totalNumbers + 1):
    # Initialize divisor count
    divisorCount = 0
    # Set numerator to the current number being checked
    numerator = currentNumber
    
    # Check each potential divisor from 2 up to currentNumber
    for potentialDivisor in range(2, currentNumber):
        # Check if numerator is divisible by potentialDivisor
        if numerator % potentialDivisor == 0:
            # Increment the divisorCount
            divisorCount += 1
            # Divide out all factors of potentialDivisor from numerator
            while numerator % potentialDivisor == 0:
                numerator //= potentialDivisor

    # Check if the current number is prime (has exactly 2 divisors)
    if divisorCount == 1 and currentNumber > 1:
        primeCount += 1  # Increment prime count if it is prime

# Output the total number of prime numbers found
print(primeCount)
