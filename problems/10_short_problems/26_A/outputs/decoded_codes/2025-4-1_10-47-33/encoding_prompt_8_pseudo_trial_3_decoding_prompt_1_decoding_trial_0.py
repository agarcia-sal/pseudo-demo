# BEGIN

# Get the input value for t
t = int(input())

# Initialize a variable to keep track of the count of semiprimes
semiprimeCount = 0

# Loop through each number from 1 to t
for i in range(1, t + 1):
    # Initialize a count for the number of distinct prime factors
    distinctPrimeCount = 0
    # Copy the current number to a temporary variable for manipulation
    currentNumber = i

    # Check for factors starting from 2
    for j in range(2, i):
        # If j is a factor of the currentNumber
        if currentNumber % j == 0:
            # Increment the count of distinct prime factors
            distinctPrimeCount += 1
            
            # Continue dividing currentNumber by j until it no longer divides evenly
            while currentNumber % j == 0:
                currentNumber //= j
            # End WHILE
        # End IF
    # End FOR

    # After checking all possible factors
    # If the number has exactly two distinct prime factors, it is a semiprime
    if distinctPrimeCount == 2:
        # Increment the semiprime count
        semiprimeCount += 1
    # End IF
# End FOR

# Output the total count of semiprimes found
print(semiprimeCount)

# END
