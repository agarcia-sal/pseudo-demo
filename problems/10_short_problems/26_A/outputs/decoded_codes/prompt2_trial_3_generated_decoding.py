# Start
t = int(input())  # Receive an integer input t which is the upper limit
resultCount = 0   # Initialize a variable resultCount to zero

# For each integer currentNumber from 1 to t
for currentNumber in range(1, t + 1):
    divisorCount = 0  # Set a variable divisorCount to zero
    tempNumber = currentNumber  # Set tempNumber equal to currentNumber

    # For each integer potentialDivisor from 2 to currentNumber - 1
    for potentialDivisor in range(2, currentNumber):
        # Check if tempNumber is divisible by potentialDivisor
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1  # Increment divisorCount by one
            
            # Continue dividing tempNumber by potentialDivisor
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor  # Factor out potentialDivisor completely

    # After checking all potential divisors
    if divisorCount == 2:  # If divisorCount equals 2
        resultCount += 1  # Increment resultCount by one

# After looping through all numbers
print(resultCount)  # Output the value of resultCount
# End
