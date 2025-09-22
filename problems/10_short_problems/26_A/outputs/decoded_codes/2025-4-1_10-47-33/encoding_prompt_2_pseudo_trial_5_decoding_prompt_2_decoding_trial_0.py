# Step 1: Receive an integer input called totalNumbers
totalNumbers = int(input())

# Step 2: Initialize a variable primeCount to zero
primeCount = 0

# Step 3: For each integer currentNumber from 1 to totalNumbers (inclusive)
for currentNumber in range(1, totalNumbers + 1):
    # Set a counter divisorCount to zero
    divisorCount = 0
    # Set a variable numerator to currentNumber
    numerator = currentNumber

    # Step 4: For each integer potentialDivisor starting from 2 up to (but not including) currentNumber
    for potentialDivisor in range(2, currentNumber):
        # Check if numerator is divisible by potentialDivisor
        if numerator % potentialDivisor == 0:
            # If it is, increment divisorCount by 1
            divisorCount += 1
            # While numerator is still divisible by potentialDivisor
            while numerator % potentialDivisor == 0:
                # Divide numerator by potentialDivisor
                numerator //= potentialDivisor

    # Step 5: Check if divisorCount equals 2
    if divisorCount == 1:  
        # If it does, increment primeCount by 1 
        primeCount += 1
        
# Step 6: Output the value of primeCount
print(primeCount)
