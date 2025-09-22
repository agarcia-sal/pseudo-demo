# Start of the program
# Read an integer input 'timePeriod' 
timePeriod = int(input())

# Initialize 'resultCount' to track numbers with exactly two distinct prime factors
resultCount = 0

# Loop through each integer 'currentNumber' from 1 to 'timePeriod' (inclusive)
for currentNumber in range(1, timePeriod + 1):
    # Initialize 'divisorCount' to track the number of distinct prime factors
    divisorCount = 0
    # Set 'tempNumber' to 'currentNumber' to manipulate during factorization
    tempNumber = currentNumber
    
    # Loop through each integer 'potentialDivisor' from 2 to 'currentNumber' - 1
    for potentialDivisor in range(2, currentNumber):
        # Check if 'tempNumber' is divisible by 'potentialDivisor'
        if tempNumber % potentialDivisor == 0:
            # Increment 'divisorCount' as we found a valid divisor
            divisorCount += 1
            # While 'tempNumber' is divisible by 'potentialDivisor', divide it
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor
    
    # Check if 'divisorCount' equals 2, indicating exactly two distinct prime factors
    if divisorCount == 2:
        # Increment 'resultCount'
        resultCount += 1

# Print the total count of numbers with exactly two distinct prime factors
print(resultCount)
# End of the program
