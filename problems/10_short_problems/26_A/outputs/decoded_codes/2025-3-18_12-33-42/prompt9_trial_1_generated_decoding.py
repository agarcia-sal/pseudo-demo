# Receive Input: Get the total count of numbers to check from the user
totalCount = int(input())

# Initialize Result Counter: Counter for prime numbers
primeCount = 0

# Loop Through Each Number: Check each number from 1 to totalCount
for currentNumber in range(1, totalCount + 1):
    # Initialize divisor count for the current number
    divisorCount = 0
    # Remaining number for factorization
    remainingNumber = currentNumber

    # Check for Divisors: Loop through potential divisors
    for potentialDivisor in range(2, currentNumber):
        if remainingNumber % potentialDivisor == 0:
            # Found a divisor, increase the count
            divisorCount += 1
            # Remove that factor
            while remainingNumber % potentialDivisor == 0:
                remainingNumber //= potentialDivisor
    
    # Identify Prime Numbers: A prime number has exactly two divisors (1 and the number itself)
    if divisorCount == 1 and currentNumber > 1:  # The '1' is a special case
        primeCount += 1

# Output the Result: Print the total number of prime numbers found
print(primeCount)
