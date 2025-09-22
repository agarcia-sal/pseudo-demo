# Start of the program

# Read an integer value which represents the upper limit of the range
totalNumbers = int(input())

# Initialize a counter for prime numbers
primeCount = 0

# Iterate over each number from 1 to totalNumbers (inclusive)
for currentNumber in range(1, totalNumbers + 1):
    # Initialize divisor count for the current number
    divisorCount = 0
    # Set tempNumber to currentNumber for checking divisibility
    tempNumber = currentNumber
    
    # Check for divisibility for numbers from 2 to currentNumber - 1
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:  # Check divisibility
            divisorCount += 1  # Found a divisor
            # While tempNumber is divisible by potentialDivisor, divide it
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor

    # Determine if the current number is prime
    if divisorCount == 1:  # 1 divisor found which is the number itself
        primeCount += 1  # Increment prime count

# Output the result
print(primeCount)

# End of the program
