# Step 1: Read an integer input for totalCount
totalCount = int(input())

# Step 2: Initialize resultCount to zero
resultCount = 0

# Step 3: Loop from 1 to totalCount (inclusive)
for currentNumber in range(1, totalCount + 1):
    # Initialize divisorCount to track distinct prime factors
    divisorCount = 0
    # Step 3.1: Loop for possible divisors starting from 2
    for divisor in range(2, currentNumber):
        # Check if currentNumber is divisible by the current divisor
        if currentNumber % divisor == 0:
            divisorCount += 1  # Increment the count of distinct prime factors
            
            # Step 3.1.1: Nested loop to divide currentNumber by the divisor
            while currentNumber % divisor == 0:
                currentNumber //= divisor  # Reduce currentNumber by the divisor
    
    # Step 4: Check if divisorCount is equal to 2
    if divisorCount == 2:
        resultCount += 1  # Increment resultCount if the condition is met

# Step 5: Output the final value of resultCount
print(resultCount)
