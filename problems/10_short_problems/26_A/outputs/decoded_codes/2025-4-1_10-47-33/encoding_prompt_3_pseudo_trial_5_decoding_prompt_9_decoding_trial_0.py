# Start of the program
timePeriod = int(input())  # Read an integer input 'timePeriod'
resultCount = 0  # Initialize 'resultCount' to 0

# Iterate over each integer 'currentNumber' from 1 to 'timePeriod' (inclusive)
for currentNumber in range(1, timePeriod + 1):
    divisorCount = 0  # Initialize 'divisorCount' to 0
    tempNumber = currentNumber  # Set 'tempNumber' to 'currentNumber'

    # Iterate over potential divisors from 2 to 'currentNumber' - 1
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:  # Check if 'tempNumber' is divisible by 'potentialDivisor'
            divisorCount += 1  # Increment 'divisorCount' by 1
            
            # While 'tempNumber' is divisible by 'potentialDivisor'
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor  # Divide 'tempNumber' by 'potentialDivisor'
    
    # If 'divisorCount' equals 2, it's indicative of two distinct prime factors
    if divisorCount == 2:
        resultCount += 1  # Increment 'resultCount' by 1

print(resultCount)  # Print 'resultCount'
# End of the program
