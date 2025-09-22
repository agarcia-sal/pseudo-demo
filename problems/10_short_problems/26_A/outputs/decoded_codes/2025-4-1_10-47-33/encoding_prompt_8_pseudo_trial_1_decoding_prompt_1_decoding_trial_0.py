# Start the Program
totalCount = int(input())  # Step 1: Read an integer value from the user

# Initialize a Result Variable
countOfNumbersWithTwoDistinctPrimeFactors = 0  # Step 2: Set the count to 0

# Loop Through Each Number
for currentNumber in range(1, totalCount + 1):  # Step 3: Loop from 1 to totalCount
    distinctPrimeFactorsCount = 0  # Initialize count of distinct prime factors
    workingNumber = currentNumber  # Store the original value

    # Check for Prime Factors
    for potentialFactor in range(2, currentNumber):  # Loop for potential prime factors
        if workingNumber % potentialFactor == 0:  # Check if divisible
            distinctPrimeFactorsCount += 1  # Increment distinct prime factors count
            while workingNumber % potentialFactor == 0:  # While still divisible
                workingNumber //= potentialFactor  # Remove the factor from workingNumber

    # Check for Two Distinct Factors
    if distinctPrimeFactorsCount == 2:  # If there are exactly two distinct prime factors
        countOfNumbersWithTwoDistinctPrimeFactors += 1  # Increment the final count

# Output the Result
print(countOfNumbersWithTwoDistinctPrimeFactors)  # Print the final count
