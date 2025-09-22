# Start Program

# Step 2: Receive Input
limit = int(input())

# Step 3: Initialize Count
countOfProducts = 0

# Step 4: Iterate Through Numbers
for currentNumber in range(1, limit + 1):
    distinctPrimeFactors = 0  # Initialize the count of distinct prime factors
    temporaryNumber = currentNumber  # Store the current number for factorization

    # Step 5: Check for Prime Factors
    for potentialPrime in range(2, currentNumber):
        if temporaryNumber % potentialPrime == 0:  # Check if potentialPrime is a factor
            distinctPrimeFactors += 1  # Found a distinct prime factor
            # Step 5.2: Remove the prime factor from temporaryNumber
            while temporaryNumber % potentialPrime == 0:
                temporaryNumber //= potentialPrime

    # Step 6: Check the Condition
    if distinctPrimeFactors == 2:  # Check if there are exactly two distinct prime factors
        countOfProducts += 1  # Increment the count

# Step 7: Output Result
print(countOfProducts)  # Output the total count of products of exactly two distinct prime numbers

# End Program
