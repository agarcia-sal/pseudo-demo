# Step 1: Obtain input for maximum number
maximumNumber = int(input())

# Step 2: Initialize result counter
result = 0

# Step 3: Loop through each integer from 1 to maximumNumber inclusive
for currentNumber in range(1, maximumNumber + 1):
    # Initialize divisor count and working number
    divisorCount = 0
    workingNumber = currentNumber

    # Step 4: Loop through potential factors starting from 2
    for potentialFactor in range(2, currentNumber):
        # Check if workingNumber is divisible by potentialFactor
        if workingNumber % potentialFactor == 0:
            # Increment divisorCount for new prime factor found
            divisorCount += 1
            
            # Eliminate potentialFactor from workingNumber
            while workingNumber % potentialFactor == 0:
                workingNumber //= potentialFactor
    
    # Step 5: Check if currentNumber has exactly two distinct prime factors
    if divisorCount == 2:
        result += 1

# Step 6: Output the final result
print(result)
