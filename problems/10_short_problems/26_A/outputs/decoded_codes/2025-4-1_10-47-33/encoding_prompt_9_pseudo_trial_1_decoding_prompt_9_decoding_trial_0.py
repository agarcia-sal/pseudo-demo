# Start Program

# Get the Input:
total = int(input())  # Read an integer value representing the upper limit for finding prime numbers

# Initialize Count of Prime Numbers:
primeCount = 0  # This variable keeps track of how many prime numbers are found

# Iterate Through Possible Numbers:
for currentNumber in range(1, total + 1):  # 'total + 1' to include 'total' itself
    divisorCount = 0  # Count of divisors for the current number
    workingNum = currentNumber  # Number to check for divisibility
    
    # Check for Divisibility:
    for potentialDivisor in range(2, currentNumber):  # Check divisibility from 2 to one less than 'currentNumber'
        if workingNum % potentialDivisor == 0:  # If 'workingNum' is divisible by 'potentialDivisor'
            divisorCount += 1  # Increment divisor count
            # Divide 'workingNum' by 'potentialDivisor' until it is no longer divisible
            while workingNum % potentialDivisor == 0:
                workingNum //= potentialDivisor
    
    # Determine if Prime:
    if divisorCount == 2:  # A prime number has exactly two distinct positive divisors: 1 and itself
        primeCount += 1  # Increment the count of prime numbers

# Output Result:
print(primeCount)  # Print the total count of prime numbers found

# End Program
