# Step 1: Input
t = int(input())  # Read an integer value `t`

# Step 2: Initialize a variable
resultCount = 0  # Count of numbers with exactly two distinct prime factors

# Step 3: Iterate through potential candidates
for currentNumber in range(1, t + 1):  # Loop from 1 to t
    factorCount = 0  # Initialize factor count
    currentValue = currentNumber  # Set current value to current number
    
    # Step 4: Check for factors
    for potentialFactor in range(2, currentNumber):  # Loop from 2 to currentNumber - 1
        if currentValue % potentialFactor == 0:  # Check if potential factor is a factor of current value
            factorCount += 1  # Increment factor count
            # Remove all occurrences of this factor
            while currentValue % potentialFactor == 0:
                currentValue //= potentialFactor  # Integer division to remove factor
    
    # Step 5: Evaluate the condition
    if factorCount == 2:  # Check if there are exactly two distinct prime factors
        resultCount += 1  # Increment resultCount

# Step 6: Output
print(resultCount)  # Display the result count
