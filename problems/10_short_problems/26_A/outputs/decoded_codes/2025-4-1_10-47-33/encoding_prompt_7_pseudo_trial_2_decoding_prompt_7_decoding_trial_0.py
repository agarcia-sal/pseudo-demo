def countSemiPrimes(t):
    # Initialize a counter for the total number of semi-primes
    totalSemiPrimes = 0
    
    # Iterate through each number from 1 to t
    for i in range(1, t + 1):
        # Initialize divisorCount to count distinct prime factors
        divisorCount = 0
        currentNumber = i  # Store the current number for factorization
        
        # Check divisions from 2 to currentNumber-1
        for j in range(2, currentNumber):
            if currentNumber % j == 0:  # Check if j is a divisor of currentNumber
                divisorCount += 1  # Found a new distinct prime factor
                # Divide currentNumber by j until it is no longer divisible
                while currentNumber % j == 0:
                    currentNumber //= j
        
        # Check if we found exactly 2 distinct prime factors
        if divisorCount == 2:
            totalSemiPrimes += 1  # Increment semi-prime count
    
    # Return the total count of semi-prime numbers found
    return totalSemiPrimes

# Read input for the upper limit
t = int(input())

# Output the result of counting semi-prime numbers
result = countSemiPrimes(t)
print(result)
