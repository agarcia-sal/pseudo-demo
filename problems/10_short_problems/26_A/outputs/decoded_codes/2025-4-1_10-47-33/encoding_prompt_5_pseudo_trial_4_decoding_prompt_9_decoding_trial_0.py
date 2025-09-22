# Start of the program
limit = int(input())  # Read the upper limit as an integer
semiprimeCount = 0    # Initialize count of semiprimes

# Loop through numbers from 1 to the upper limit
for currentNumber in range(1, limit + 1):
    primeFactorCount = 0  # Initialize prime factor count for the current number
    numberToCheck = currentNumber  # Value to check for prime factors

    # Find prime factors of the current number
    for potentialPrime in range(2, currentNumber):  # Check potential primes up to currentNumber - 1
        if numberToCheck % potentialPrime == 0:  # If divisible by potential prime
            primeFactorCount += 1  # Found a prime factor
            
            # Divide numberToCheck by potentialPrime until no longer divisible
            while numberToCheck % potentialPrime == 0:
                numberToCheck //= potentialPrime  # Reduce numberToCheck

    # Check if the current number has exactly two distinct prime factors
    if primeFactorCount == 2:
        semiprimeCount += 1  # Increment semiprime count

# Output the result
print(semiprimeCount)  # Print the total count of semiprimes
