# Step 1: Input an integer value
totalCount = int(input())

# Step 2: Initialize primeCount to zero
primeCount = 0

# Step 3: Loop over each number from 1 to totalCount
for currentNumber in range(1, totalCount + 1):
    # Initialize divisorCount and workingNumber
    divisorCount = 0
    workingNumber = currentNumber
    
    # Step 4: Check for divisors
    for potentialDivisor in range(2, currentNumber):
        if workingNumber % potentialDivisor == 0:  # Check if divisible
            divisorCount += 1  # Found a divisor
            while workingNumber % potentialDivisor == 0:  # Remove the divisor
                workingNumber //= potentialDivisor  # Reduce workingNumber
            
    # Step 5: Determine if currentNumber is prime
    if divisorCount == 2:
        primeCount += 1  # Increment prime count

# Step 6: Output the total number of prime numbers found
print(primeCount)
