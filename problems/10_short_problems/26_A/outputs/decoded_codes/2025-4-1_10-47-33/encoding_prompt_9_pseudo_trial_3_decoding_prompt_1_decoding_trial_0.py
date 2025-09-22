# Step 1: Start the program and read an integer t from the user
t = int(input())

# Step 2: Initialize semiprimeCount to 0
semiprimeCount = 0

# Step 3: Loop through each number from 1 to t (inclusive)
for currentNumber in range(1, t + 1):
    # Set distinctPrimeCount to 0
    distinctPrimeCount = 0
    # Set number equal to currentNumber
    number = currentNumber

    # Step 4: Loop through each potential factor starting from 2 up to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        # Check if currentNumber is divisible by potentialFactor
        if currentNumber % potentialFactor == 0:
            # If true, increase distinctPrimeCount by 1
            distinctPrimeCount += 1
            # While number is divisible by potentialFactor
            while number % potentialFactor == 0:
                # Divide number by potentialFactor
                number //= potentialFactor

    # Step 5: After checking all potential factors
    if distinctPrimeCount == 2:
        # Increase semiprimeCount by 1
        semiprimeCount += 1

# Step 6: Once all numbers have been checked, output semiprimeCount
print(semiprimeCount)
