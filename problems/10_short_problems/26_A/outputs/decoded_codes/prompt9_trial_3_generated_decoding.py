# Start of the program

# Receive Input
limit = int(input())  # Getting the limit from the user

# Initialize a Count Variable
primeCount = 0  # This will track the number of prime numbers

# Iterate Through Numbers
for currentNumber in range(1, limit + 1):
    divisorCount = 0  # Resetting divisor count for each number
    tempNumber = currentNumber  # Temporary variable to check for factors

    # Check for Factors
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:  # Check if divisible
            divisorCount += 1  # Count this divisor
            
            # Remove the factor from tempNumber
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor

    # Determine Prime Status
    if divisorCount == 2:
        primeCount += 1  # It's a prime number

# Output the Result
print(primeCount)  # Print the total count of prime numbers
