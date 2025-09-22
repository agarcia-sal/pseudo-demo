# Start Program

# Step 2: Get Input
# Read an integer value from the user and store it in the variable totalNumbers
totalNumbers = int(input())

# Step 3: Initialize Count
# Set result to 0. This variable will keep track of how many numbers meet the criteria.
result = 0

# Step 4: Iterate Through Numbers
# For each number currentNumber from 1 to totalNumbers
for currentNumber in range(1, totalNumbers + 1):
    # Step 4a: Initialize a variable primeFactorCount to 0
    primeFactorCount = 0
    # Step 4b: Set tempNumber to currentNumber to work with
    tempNumber = currentNumber

    # Step 5: Check for Prime Factors
    # For each potential factor starting from 2 up to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        # Step 5a: Check if tempNumber is divisible by potentialFactor
        if tempNumber % potentialFactor == 0:
            # Step 5a.i: Increment primeFactorCount by 1
            primeFactorCount += 1
            
            # Step 5a.ii: Remove all occurrences of this factor
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor

    # Step 6: Evaluate Condition
    # After checking all potential factors, if primeFactorCount equals 2
    if primeFactorCount == 2:
        # Increment result by 1
        result += 1

# Step 7: Output the Result
# Print the value of result
print(result)

# End Program
