# Get User Input
maximumNumber = int(input())  # Ask the user for a positive integer

# Initialize Count of Prime Numbers
primeCount = 0  # This will count the total number of prime numbers found

# Loop Through Each Number
for currentNumber in range(1, maximumNumber + 1):  # Inclusive of maximumNumber
    factorCount = 0  # Initialize a variable to count factors
    remainingNumber = currentNumber  # Set the remaining number to the current number

    # Check for Factors
    for potentialFactor in range(2, currentNumber):  # Potential factors from 2 to currentNumber - 1
        if remainingNumber % potentialFactor == 0:  # Check if divisible
            factorCount += 1  # Increase the count of factors
            # Remove the factor from remainingNumber completely
            while remainingNumber % potentialFactor == 0:
                remainingNumber //= potentialFactor  # Divide remainingNumber by potentialFactor

    # Identify Prime Number
    if factorCount == 1 and currentNumber > 1:  # A prime number has exactly two factors: 1 and the number itself
        primeCount += 1  # Increase prime count

# Output the Result
print(primeCount)  # Display the total number of prime numbers found
