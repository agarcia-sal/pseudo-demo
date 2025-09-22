# Step 1: Input
t = int(input())  # Read an integer from the user representing the upper limit

# Step 2: Initialize Result
totalCount = 0  # This will count the numbers with exactly two distinct prime factors

# Step 3: Loop Through Each Number
for currentNumber in range(1, t + 1):
    distinctPrimeCount = 0  # Track distinct prime factors for currentNumber
    currentValue = currentNumber  # Initialize currentValue with currentNumber

    # Step 4: Find Prime Factors
    for potentialPrime in range(2, currentNumber):
        # Check if currentValue is divisible by potentialPrime
        if currentValue % potentialPrime == 0:
            distinctPrimeCount += 1  # Found a new distinct prime factor
            # While currentValue is divisible by potentialPrime
            while currentValue % potentialPrime == 0:
                currentValue //= potentialPrime  # Divide currentValue by potentialPrime

    # Step 5: Check for Exactly Two Distinct Prime Factors
    if distinctPrimeCount == 2:
        totalCount += 1  # Increment count if exactly two distinct prime factors are found

# Step 6: Output the Result
print(totalCount)  # Print the total count
