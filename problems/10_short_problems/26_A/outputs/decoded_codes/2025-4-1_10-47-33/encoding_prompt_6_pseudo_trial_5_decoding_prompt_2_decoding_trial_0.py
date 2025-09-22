# Step 1: Read input
t = int(input())  # Upper limit for checking numbers from 1 to t

# Step 2: Initialize Result
totalCount = 0  # Counts numbers with exactly two distinct prime factors

# Step 3: Loop Through Each Number
for currentNumber in range(1, t + 1):
    distinctPrimeCount = 0  # Track number of distinct prime factors
    currentValue = currentNumber  # Work with the current number

    # Step 4: Find Prime Factors
    for potentialPrime in range(2, currentNumber):  # Check potential primes
        if currentValue % potentialPrime == 0:  # Check divisibility
            distinctPrimeCount += 1  # Found a new distinct prime factor
            
            # While loop to divide out all occurrences of the prime factor
            while currentValue % potentialPrime == 0:
                currentValue //= potentialPrime  # Reduce currentValue

    # Step 5: Check for Exactly Two Distinct Prime Factors
    if distinctPrimeCount == 2:
        totalCount += 1  # Increment count if exactly two distinct primes are found

# Step 6: Output the Result
print(totalCount)  # Output the total count
