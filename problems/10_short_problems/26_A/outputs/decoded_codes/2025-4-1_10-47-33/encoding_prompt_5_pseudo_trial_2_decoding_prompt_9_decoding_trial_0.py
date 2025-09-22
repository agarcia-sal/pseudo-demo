# Get the upper limit for counting prime numbers
t = int(input())

# Initialize a counter for prime numbers
primeCount = 0

# Loop through each number from 1 to t
for currentNumber in range(1, t + 1):
    # Initialize the divisor count
    divisorCount = 0
    # Set the remaining value to the current number
    remainingValue = currentNumber
    
    # Check for potential divisors
    for potentialDivisor in range(2, currentNumber):
        # If the remaining value is divisible by the potential divisor
        if remainingValue % potentialDivisor == 0:
            # Increment the divisor count
            divisorCount += 1
            # While the remaining value is divisible by the potential divisor
            while remainingValue % potentialDivisor == 0:
                # Divide remaining value by the potential divisor
                remainingValue //= potentialDivisor
    
    # Check if the current number is prime (2 divisors: 1 and itself)
    if divisorCount == 2:
        primeCount += 1

# Output the final count of prime numbers found
print(primeCount)
