# Input the number of test cases:
t = int(input())

# Initialize a variable to hold the count of prime numbers:
resultCount = 0

# Process each number from 1 to t:
for currentNumber in range(1, t + 1):
    # Initialize a variable divisor count:
    divisorCount = 0
    remainingNumber = currentNumber
    
    # Check for prime factors:
    for potentialDivisor in range(2, currentNumber):
        # If remainingNumber is divisible by potentialDivisor:
        if remainingNumber % potentialDivisor == 0:
            divisorCount += 1
            # Factor out potentialDivisor completely:
            while remainingNumber % potentialDivisor == 0:
                remainingNumber //= potentialDivisor
    
    # Check if the current number is prime:
    if divisorCount == 2:
        resultCount += 1

# Output the total count of prime numbers:
print(resultCount)
