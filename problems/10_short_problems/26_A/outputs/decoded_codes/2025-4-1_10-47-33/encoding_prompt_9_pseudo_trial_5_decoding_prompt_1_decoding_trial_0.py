# 1. Start by Receiving Input
t = int(input())

# 2. Initialize a Counter for Semiprimes
semiprimeCount = 0

# 3. Loop Through Each Number from 1 to t
for currentNumber in range(1, t + 1):
    # Initialize a counter for prime factors
    primeFactorCount = 0
    dividedNumber = currentNumber  # Set this to the current number

    # 4. Identify Prime Factors for the Current Number
    for possibleFactor in range(2, currentNumber):  # Iterate from 2 to currentNumber - 1
        if dividedNumber % possibleFactor == 0:
            primeFactorCount += 1  # Found a prime factor
            # While dividedNumber is still divisible by possibleFactor
            while dividedNumber % possibleFactor == 0:
                dividedNumber //= possibleFactor  # Divide out the prime factor

    # 5. Check for Semiprime Condition
    if primeFactorCount == 2:
        semiprimeCount += 1  # Increment count if it's a semiprime

# 6. Output the Result
print(semiprimeCount)  # Print the total count of semiprime numbers
