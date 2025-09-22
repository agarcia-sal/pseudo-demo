# Start
limit = int(input())  # Read an integer value as the upper limit (referred to as limit)

# Initialize Count
semiprimeCount = 0  # Set a variable called semiprimeCount to 0

# Loop through Numbers
for currentNumber in range(1, limit + 1):  # For each integer currentNumber starting from 1 up to limit (inclusive)
    primeFactorCount = 0  # Initialize a variable primeFactorCount to 0
    numberToCheck = currentNumber  # Set numberToCheck to the value of currentNumber

    # Find Prime Factors
    for potentialPrime in range(2, currentNumber):  # For each integer potentialPrime starting from 2 up to (currentNumber - 1)
        if numberToCheck % potentialPrime == 0:  # Check if numberToCheck is divisible by potentialPrime
            primeFactorCount += 1  # Increment primeFactorCount by 1
            while numberToCheck % potentialPrime == 0:  # While numberToCheck is still divisible by potentialPrime
                numberToCheck //= potentialPrime  # Divide numberToCheck by potentialPrime

    # Check for Semiprime
    if primeFactorCount == 2:  # Check if primeFactorCount equals 2
        semiprimeCount += 1  # Increment semiprimeCount by 1

# Output Result
print(semiprimeCount)  # Print the value of semiprimeCount
