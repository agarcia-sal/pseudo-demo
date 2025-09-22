# Step 1: Accept input for the total number of natural numbers to evaluate
totalNumbers = int(input())

# Step 2: Initialize the count of special numbers
countOfSpecialNumbers = 0

# Step 3: Loop from 1 to totalNumbers, inclusive
for currentNumber in range(1, totalNumbers + 1):
    # Initialize a counter for distinct divisors
    divisorCount = 0
    # Step 4: Loop from 2 to currentNumber - 1 to find divisors
    for divisor in range(2, currentNumber):
        if currentNumber % divisor == 0:
            # If divisible, increment the divisor count
            divisorCount += 1
            # Continue dividing by this divisor until no longer divisible
            while currentNumber % divisor == 0:
                currentNumber //= divisor
    
    # Step 5: Check if we found exactly two distinct prime factors
    if divisorCount == 2:
        countOfSpecialNumbers += 1

# Step 6: Output the count of special numbers
print(countOfSpecialNumbers)
