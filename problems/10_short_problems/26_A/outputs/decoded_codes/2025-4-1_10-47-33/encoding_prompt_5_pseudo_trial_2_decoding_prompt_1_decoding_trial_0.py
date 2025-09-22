# Step 1: Get Input
t = int(input())  # Getting integer input from user and casting to int

# Step 2: Initialize a Counter
primeCount = 0  # Counter for prime numbers

# Step 3: Loop Through Each Number
for currentNumber in range(1, t + 1):  # Looping from 1 to t inclusive
    divisorCount = 0  # Initialize divisor count for currentNumber
    remainingValue = currentNumber  # Set remaining value to currentNumber

    # Step 4: Check for Divisibility
    for potentialDivisor in range(2, currentNumber):  # Looping potential divisors from 2 to currentNumber - 1
        if remainingValue % potentialDivisor == 0:  # If remainingValue is divisible by potentialDivisor
            divisorCount += 1  # Increment the divisor count
            while remainingValue % potentialDivisor == 0:  # While divisible
                remainingValue //= potentialDivisor  # Divide remainingValue by potentialDivisor

    # Step 5: Determine if Prime
    if divisorCount == 2:  # Check if the number is prime
        primeCount += 1  # Increment prime count

# Step 6: Output Result
print(primeCount)  # Display the final count of prime numbers
