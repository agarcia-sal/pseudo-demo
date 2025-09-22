# Start Program

# Get the Input
total = int(input())  # Read an integer value from the user

# Initialize Count of Prime Numbers
primeCount = 0  # This will keep track of how many prime numbers are found

# Iterate Through Possible Numbers
for currentNumber in range(1, total + 1):  # Current number from 1 to total
    divisorCount = 0  # Count of divisors for the current number
    workingNum = currentNumber  # Working number to check for divisibility

    # Check for Divisibility
    for potentialDivisor in range(2, workingNum):  # Check from 2 to currentNumber - 1
        if workingNum % potentialDivisor == 0:  # If workingNum is divisible by potentialDivisor
            divisorCount += 1  # Increment divisor count
            # Divide workingNum by potentialDivisor until it's no longer divisible
            while workingNum % potentialDivisor == 0:
                workingNum //= potentialDivisor  # Use integer division

    # Determine if Prime
    if divisorCount == 2:  # If the current number has exactly 2 divisors (1 and itself)
        primeCount += 1  # Increment prime count

# Output Result
print(primeCount)  # Print the total number of prime numbers found

# End Program
