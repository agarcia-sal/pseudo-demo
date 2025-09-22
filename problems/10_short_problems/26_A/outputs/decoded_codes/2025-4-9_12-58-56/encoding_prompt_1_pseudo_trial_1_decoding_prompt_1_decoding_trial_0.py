# Start
t = int(input())  # Read an integer value `t` from the user.

# Initialize Result
primeCount = 0  # Set a variable called `primeCount` to 0.

# Loop Through Numbers
for currentNumber in range(1, t + 1):  # For each number `currentNumber` from 1 to `t` (inclusive).
    divisorCount = 0  # Set a variable `divisorCount` to 0.
    tempNumber = currentNumber  # Set a variable `tempNumber` to `currentNumber`.

    # Check for Divisors
    for potentialDivisor in range(2, currentNumber):  # For each number `potentialDivisor` starting from 2 up to (but not including) `currentNumber`.
        if tempNumber % potentialDivisor == 0:  # If `tempNumber` is divisible by `potentialDivisor`.
            divisorCount += 1  # Increase `divisorCount` by 1.
            while tempNumber % potentialDivisor == 0:  # While `tempNumber` is still divisible by `potentialDivisor`.
                tempNumber //= potentialDivisor  # Divide `tempNumber` by `potentialDivisor`.

    # Determine if Prime
    if divisorCount == 2:  # If `divisorCount` equals 2.
        primeCount += 1  # Increase `primeCount` by 1.

# Output Result
print(primeCount)  # Print the value of `primeCount`.
