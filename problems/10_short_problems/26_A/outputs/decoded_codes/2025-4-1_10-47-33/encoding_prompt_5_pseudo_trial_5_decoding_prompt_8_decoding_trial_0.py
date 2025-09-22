# Start

# Define the Input:
totalNumbers = int(input())

# Initialize Count:
primeCount = 0

# Iterate Over Each Number:
for currentNumber in range(1, totalNumbers + 1):
    divisorCount = 0
    tempNumber = currentNumber

    # Check for Divisibility:
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor

    # Determine If Prime:
    if divisorCount == 2:  # 1 and the number itself
        primeCount += 1

# Output the Result:
print(primeCount)

# End


import math

# Start

# Define the Input:
totalNumbers = int(input())

# Initialize Count:
primeCount = 0

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for potentialDivisor in range(2, int(math.sqrt(num)) + 1):
        if num % potentialDivisor == 0:
            return False
    return True

# Iterate Over Each Number:
for currentNumber in range(1, totalNumbers + 1):
    if is_prime(currentNumber):
        primeCount += 1

# Output the Result:
print(primeCount)

# End
