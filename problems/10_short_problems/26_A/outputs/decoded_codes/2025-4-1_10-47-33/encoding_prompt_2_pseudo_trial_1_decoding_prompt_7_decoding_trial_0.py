# Step 1: Read an integer value `t` which represents the upper limit for checking certain numbers.
t = int(input())

# Step 2: Initialize a variable `resultCount` to count numbers with exactly two distinct prime factors.
resultCount = 0

# Step 3: Iterate through potential candidates `currentNumber` from 1 to `t`.
for currentNumber in range(1, t + 1):
    # Initialize counter for distinct prime factors
    factorCount = 0
    # Set `currentValue` to `currentNumber` for factor manipulation
    currentValue = currentNumber
    
    # Step 4: Check for factors starting from 2 up to one less than `currentNumber`
    for potentialFactor in range(2, currentNumber):
        # If `currentValue` is divisible by `potentialFactor`
        if currentValue % potentialFactor == 0:
            # Increment the factor count as we found a new factor
            factorCount += 1
            
            # Remove all instances of this factor from currentValue
            while currentValue % potentialFactor == 0:
                currentValue //= potentialFactor
    
    # Step 5: Evaluate the condition of having exactly two distinct prime factors
    if factorCount == 2:
        # Increment resultCount for a successful candidate
        resultCount += 1

# Step 6: Output the total count of integers with exactly two distinct prime factors
print(resultCount)
