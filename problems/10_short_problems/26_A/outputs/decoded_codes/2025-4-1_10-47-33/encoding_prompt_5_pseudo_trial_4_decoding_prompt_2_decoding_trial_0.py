# Start
limit = int(input())  # Read an integer value as the upper limit
semiprimeCount = 0  # Initialize Count

# Loop through Numbers
for currentNumber in range(1, limit + 1):
    primeFactorCount = 0  # Initialize prime factor count
    numberToCheck = currentNumber  # Set number to check

    # Find Prime Factors
    for potentialPrime in range(2, currentNumber):  # Starting from 2 to currentNumber - 1
        if numberToCheck % potentialPrime == 0:  # Check divisibility
            primeFactorCount += 1  # Increment prime factor count
            
            # While still divisible, divide numberToCheck
            while numberToCheck % potentialPrime == 0:
                numberToCheck //= potentialPrime  # Reduce numberToCheck

    # Check for Semiprime
    if primeFactorCount == 2:  # If there are exactly 2 prime factors
        semiprimeCount += 1  # Increment semiprime count

# Output Result
print(semiprimeCount)  # Print the count of semiprime numbers
