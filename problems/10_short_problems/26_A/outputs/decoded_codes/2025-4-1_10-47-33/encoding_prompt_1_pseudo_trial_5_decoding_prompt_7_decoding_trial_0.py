# Step 1: Read an integer input value 't' which represents the upper limit for checking numbers.
t = int(input())

# Step 2: Initialize a variable 'resultCount' to 0.
resultCount = 0

# Step 3: For each number 'currentNumber' from 1 to 't'
for currentNumber in range(1, t + 1):
    # Initialize a variable 'distinctPrimeFactorsCount' to 0.
    distinctPrimeFactorsCount = 0
    # Set 'tempNumber' to 'currentNumber' which will be manipulated to find the prime factors.
    tempNumber = currentNumber

    # Step 3.4: For each integer 'potentialFactor' starting from 2 up to but not including 'currentNumber'
    for potentialFactor in range(2, currentNumber):
        # Check if 'tempNumber' is divisible by 'potentialFactor'
        if tempNumber % potentialFactor == 0:
            # If it is divisible, increment 'distinctPrimeFactorsCount' by 1.
            distinctPrimeFactorsCount += 1
            
            # While 'tempNumber' is still divisible by 'potentialFactor'
            while tempNumber % potentialFactor == 0:
                # Divide 'tempNumber' by 'potentialFactor'
                tempNumber //= potentialFactor

    # Step 4: After checking all 'potentialFactor's
    # If 'distinctPrimeFactorsCount' equals 2, it means 'currentNumber' has exactly two distinct prime factors
    if distinctPrimeFactorsCount == 2:
        # Increment 'resultCount' by 1.
        resultCount += 1

# Step 5: Output the value of 'resultCount'
print(resultCount)
