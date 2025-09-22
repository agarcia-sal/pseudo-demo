# Start of the program

# Step 2: Define the Input
# Read an integer value called totalNumbers which represents the upper limit of the range
totalNumbers = int(input())

# Step 3: Initialize Count
# Set a variable primeCount to 0. This will keep track of the number of prime numbers found
primeCount = 0

# Step 4: Iterate Over Each Number
# For each integer currentNumber from 1 to totalNumbers (inclusive)
for currentNumber in range(1, totalNumbers + 1):
    
    # Initialize divisor count for current number
    divisorCount = 0
    tempNumber = currentNumber  # This will be used to check for divisibility
    
    # Step 5: Check for Divisibility
    # For each integer potentialDivisor from 2 to currentNumber - 1
    for potentialDivisor in range(2, currentNumber):
        
        # If tempNumber is divisible by potentialDivisor
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1  # Increase divisor count
            
            # While tempNumber is still divisible by potentialDivisor
            while tempNumber % potentialDivisor == 0:
                # Divide tempNumber by potentialDivisor
                tempNumber //= potentialDivisor

    # Step 6: Determine If Prime
    # If divisorCount equals 2
    if divisorCount == 1 and currentNumber > 1:  # Must ensure currentNumber > 1 for prime check
        primeCount += 1  # Increase primeCount as currentNumber is prime

# Step 7: Output the Result
# Print the value of primeCount
print(primeCount)

# End of the program
