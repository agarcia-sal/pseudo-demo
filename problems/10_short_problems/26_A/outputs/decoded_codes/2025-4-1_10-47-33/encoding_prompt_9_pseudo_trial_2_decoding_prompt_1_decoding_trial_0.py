# Step 1: Get User Input
maximumNumber = int(input())  # Ask the user to enter a positive integer

# Step 2: Initialize Count of Prime Numbers
primeCount = 0  # This will hold the total number of prime numbers found

# Step 3: Loop Through Each Number
for currentNumber in range(1, maximumNumber + 1):  # Loop from 1 to maximumNumber
    factorCount = 0  # Initialize the count of factors for currentNumber
    remainingNumber = currentNumber  # Start with the number itself

    # Step 4: Check for Factors
    for potentialFactor in range(2, currentNumber):  # Check factors from 2 to currentNumber - 1
        if remainingNumber % potentialFactor == 0:  # Check if divisible
            factorCount += 1  # Increase factor count
            # While loop to remove all instances of potential factor
            while remainingNumber % potentialFactor == 0:
                remainingNumber //= potentialFactor  # Divide remaining number by potential factor

    # Step 5: Identify Prime Number
    if factorCount == 1 and currentNumber > 1:  # A prime number has exactly two distinct factors: 1 and itself
        primeCount += 1  # Increase prime count

# Step 6: Output the Result
print(primeCount)  # Output the total number of prime numbers
