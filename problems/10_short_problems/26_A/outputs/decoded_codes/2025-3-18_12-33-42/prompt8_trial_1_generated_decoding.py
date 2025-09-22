# Start Program

# Define Input
t = int(input())

# Initialize Result
totalCount = 0

# Loop Through Numbers
for currentNumber in range(1, t + 1):
    distinctPrimeCount = 0
    divisor = 2  # the smallest prime number
    
    # Inner Loop for Prime Factors
    tempNumber = currentNumber  # Use a temporary variable to factor out primes
    while divisor < tempNumber:
        if tempNumber % divisor == 0:
            distinctPrimeCount += 1
            
            # Reduce currentNumber
            while tempNumber % divisor == 0:
                tempNumber //= divisor
        
        divisor += 1  # check the next potential prime factor

    # Check Distinct Prime Condition
    if distinctPrimeCount == 2:
        totalCount += 1  # currentNumber is the product of two distinct primes

# Output Result
print(totalCount)

# End Program
