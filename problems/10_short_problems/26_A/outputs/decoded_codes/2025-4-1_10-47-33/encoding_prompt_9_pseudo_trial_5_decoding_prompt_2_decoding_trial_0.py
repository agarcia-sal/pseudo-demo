# Step 1: Start by Receiving Input
t = int(input())  # Get a number representing the upper limit

# Step 2: Initialize a Counter for Semiprimes
semiprimeCount = 0  # Variable to keep track of the number of semiprimes

# Step 3: Loop Through Each Number from 1 to t
for currentNumber in range(1, t + 1):
    primeFactorCount = 0  # Counter for distinct prime factors
    dividedNumber = currentNumber  # This will be divided by its prime factors

    # Step 4: Identify Prime Factors for the Current Number
    for possibleFactor in range(2, currentNumber):  # Potential factors starting from 2 up to less than currentNumber
        if dividedNumber % possibleFactor == 0:  # If divisible by possibleFactor
            primeFactorCount += 1  # Increment the count of prime factors
            # While dividedNumber is still divisible by possibleFactor
            while dividedNumber % possibleFactor == 0:
                dividedNumber //= possibleFactor  # Divide out the factor
            
    # Step 5: Check for Semiprime Condition
    if primeFactorCount == 2:  # Exactly 2 distinct prime factors means it's a semiprime
        semiprimeCount += 1  # Increment the count of semiprime numbers

# Step 6: Output the Result
print(semiprimeCount)  # Print the total count of semiprime numbers
