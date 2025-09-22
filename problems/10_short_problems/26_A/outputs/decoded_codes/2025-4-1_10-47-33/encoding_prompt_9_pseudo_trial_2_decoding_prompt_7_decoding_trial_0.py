# Purpose: Count and output the number of prime numbers up to a specified integer

# Step 1: Get User Input
maximumNumber = int(input())  # Read a positive integer from user input

# Step 2: Initialize Count of Prime Numbers
primeCount = 0  # Variable to hold the total number of prime numbers found

# Step 3: Loop Through Each Number from 1 to maximumNumber
for currentNumber in range(2, maximumNumber + 1):  # Start from 2, as 1 is not prime
    factorCount = 0  # Initialize factor count for current number
    remainingNumber = currentNumber  # Copy current number for factorization

    # Step 4: Check for Factors
    for potentialFactor in range(2, currentNumber):  # Check potential factors
        if remainingNumber % potentialFactor == 0:  # Check if factor divides the number
            factorCount += 1  # Increment count of factors
            # While the remaining number is divisible by the factor
            while remainingNumber % potentialFactor == 0:
                remainingNumber //= potentialFactor  # Remove the factor

    # Step 5: Identify Prime Number
    if factorCount == 1:  # A prime number has exactly one unique factor (itself)
        primeCount += 1  # Increment prime count

# Step 6: Output the Result
print(primeCount)  # Output the total number of prime numbers found
