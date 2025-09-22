# Step 1: Read an integer input representing the maximum number to check
limit = int(input())

# Step 2: Initialize a variable to count numbers with exactly two unique prime factors
resultCount = 0

# Step 3: Loop through each integer from 1 to limit (inclusive)
for currentNumber in range(1, limit + 1):
    # Step 3a: Initialize factorCount to count unique prime factors
    factorCount = 0
    # Step 3b: Set tempNumber to the current number being checked
    tempNumber = currentNumber
    
    # Step 3c: Loop through potential factors starting from 2 up to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        # Step 3c.i: Check if tempNumber is divisible by potentialFactor
        if tempNumber % potentialFactor == 0:
            # Increment factorCount to indicate a new unique prime factor found
            factorCount += 1
            
            # Step 3c.ii: While tempNumber is still divisible by potentialFactor
            while tempNumber % potentialFactor == 0:
                # Divide tempNumber by potentialFactor to eliminate that factor
                tempNumber //= potentialFactor
    
    # Step 3d: Check if the number of unique factors is exactly 2
    if factorCount == 2:
        # Increment resultCount if the condition is met
        resultCount += 1

# Step 4: Output the final count of numbers with exactly two unique prime factors
print(resultCount)
