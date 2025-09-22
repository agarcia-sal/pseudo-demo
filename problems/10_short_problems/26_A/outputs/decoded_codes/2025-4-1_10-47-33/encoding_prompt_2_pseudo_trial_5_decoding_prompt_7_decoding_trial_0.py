# Step 1: Receive an integer input for total numbers to check for primes
totalNumbers = int(input())

# Step 2: Initialize primeCount to keep track of prime numbers found
primeCount = 0

# Step 3: Loop through each integer from 1 to totalNumbers (inclusive)
for currentNumber in range(1, totalNumbers + 1):
    # Initialize the counter for distinct divisors
    divisorCount = 0
    # Store the current number for checking divisibility
    numerator = currentNumber
    
    # Step 4: Check potential divisors from 2 to currentNumber - 1
    for potentialDivisor in range(2, currentNumber):
        # Check if numerator is divisible by potentialDivisor
        if numerator % potentialDivisor == 0:
            # If it is divisible, increment divisorCount
            divisorCount += 1
            # Divide numerator by potentialDivisor to remove all factors
            while numerator % potentialDivisor == 0:
                numerator //= potentialDivisor
                
    # Step 5: After checking divisors, check if we found exactly 2 distinct divisors
    if divisorCount == 2:
        # If so, currentNumber is prime, increment primeCount
        primeCount += 1

# Step 6: Output the total number of prime numbers found
print(primeCount)
