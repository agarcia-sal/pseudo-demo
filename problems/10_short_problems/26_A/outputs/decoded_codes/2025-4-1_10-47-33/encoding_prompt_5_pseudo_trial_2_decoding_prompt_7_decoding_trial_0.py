# Step 1: Get Input
# Prompt the user to enter an integer value for t
t = int(input())

# Step 2: Initialize a Counter
# Initialize the count of prime numbers found
primeCount = 0

# Step 3: Loop Through Each Number
for currentNumber in range(1, t + 1):
    # Initialize divisor count and remaining value
    divisorCount = 0
    remainingValue = currentNumber

    # Step 4: Check for Divisibility
    for potentialDivisor in range(2, currentNumber):
        if remainingValue % potentialDivisor == 0:
            # Found a divisor, increase the count
            divisorCount += 1
            
            # Remove all occurrences of potentialDivisor from remainingValue
            while remainingValue % potentialDivisor == 0:
                remainingValue //= potentialDivisor

    # Step 5: Determine if Prime
    if divisorCount == 1 and currentNumber > 1:  # Adjusted condition for primes
        primeCount += 1

# Step 6: Output Result
# Print the final count of prime numbers found
print(primeCount)
