# Read an integer input value t which represents the upper limit for checking numbers.
t = int(input())

# Initialize a variable resultCount to 0. This will keep track of how many numbers 
# from 1 to t have exactly two distinct prime factors.
resultCount = 0

# For each number currentNumber from 1 to t:
for currentNumber in range(1, t + 1):
    # Initialize a variable distinctPrimeFactorsCount to 0.
    distinctPrimeFactorsCount = 0
    # Set tempNumber to currentNumber which will be manipulated to find the prime factors.
    tempNumber = currentNumber

    # For each integer potentialFactor starting from 2 up to but not including currentNumber:
    for potentialFactor in range(2, currentNumber):
        # Check if tempNumber is divisible by potentialFactor:
        if tempNumber % potentialFactor == 0:
            # If it is divisible:
            distinctPrimeFactorsCount += 1

            # While tempNumber is still divisible by potentialFactor:
            while tempNumber % potentialFactor == 0:
                # Repeatedly divide tempNumber by potentialFactor.
                tempNumber //= potentialFactor

    # After checking all potentialFactor's:
    # If distinctPrimeFactorsCount equals 2:
    if distinctPrimeFactorsCount == 2:
        # Increment resultCount by 1.
        resultCount += 1

# After checking all numbers from 1 to t, output the value of resultCount.
print(resultCount)
