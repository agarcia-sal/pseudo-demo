# Step 1: Read an integer input value t
t = int(input())

# Step 2: Initialize a variable resultCount to 0
resultCount = 0

# Step 3: For each number currentNumber from 1 to t
for currentNumber in range(1, t + 1):
    # Initialize distinctPrimeFactorsCount to 0
    distinctPrimeFactorsCount = 0
    # Set tempNumber to currentNumber
    tempNumber = currentNumber
    
    # For each integer potentialFactor starting from 2 up to but not including currentNumber
    for potentialFactor in range(2, currentNumber):
        # Check if tempNumber is divisible by potentialFactor
        if tempNumber % potentialFactor == 0:
            # If it is divisible, increment distinctPrimeFactorsCount by 1
            distinctPrimeFactorsCount += 1
            # While tempNumber is still divisible by potentialFactor
            while tempNumber % potentialFactor == 0:
                # Repeatedly divide tempNumber by potentialFactor
                tempNumber //= potentialFactor

    # After checking all potentialFactors:
    # If distinctPrimeFactorsCount equals 2
    if distinctPrimeFactorsCount == 2:
        # Increment resultCount by 1
        resultCount += 1

# Step 4: Output the value of resultCount
print(resultCount)
