# Start by receiving input
t = int(input())  # Get an upper limit from the user

# Initialize a counter for semiprimes
semiprimeCount = 0

# Loop through each number from 1 to t
for currentNumber in range(1, t + 1):
    # Initialize a counter for prime factors
    primeFactorCount = 0
    dividedNumber = currentNumber  # This will be used for division

    # Identify prime factors for the current number
    for possibleFactor in range(2, currentNumber):
        if dividedNumber % possibleFactor == 0:  # Check if it divides evenly
            primeFactorCount += 1  # Found a prime factor
            
            # Divide 'dividedNumber' by 'possibleFactor' while it is divisible
            while dividedNumber % possibleFactor == 0:
                dividedNumber //= possibleFactor  # Use floor division

    # Check for semiprime condition
    if primeFactorCount == 2:
        semiprimeCount += 1  # Increment the semiprime count

# Output the result
print(semiprimeCount)  # Print the total count of semiprimes
