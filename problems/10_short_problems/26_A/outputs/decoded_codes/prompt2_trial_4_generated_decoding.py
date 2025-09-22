# Step 1: Accept an integer input for the total number to check for prime numbers
totalNumbers = int(input())

# Step 2: Initialize a counter for prime numbers
primeCount = 0

# Step 3: Loop through each number from 1 to totalNumbers
for currentNumber in range(1, totalNumbers + 1):
    # Initialize a counter for divisors
    divisorCount = 0
    # Temporary variable to check divisibility
    tempNumber = currentNumber
    
    # Step 4: Check for divisors of currentNumber
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:
            # Increment divisorCount if divisible
            divisorCount += 1
            # Continue dividing tempNumber by potentialDivisor
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor
    
    # Step 5: Determine if currentNumber is prime
    if divisorCount == 2:  # It has exactly two distinct divisors: 1 and itself
        primeCount += 1

# Step 6: Output the total count of prime numbers
print(primeCount)
