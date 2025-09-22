# Function to count numbers which are products of exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read totalCount from user input
    totalCount = int(input())  # Input is expected to be an integer variable

    # Step 2: Initialize the result variable
    countOfNumbersWithTwoDistinctPrimeFactors = 0  # This will hold our result count

    # Step 3: Loop through each number from 1 to totalCount
    for currentNumber in range(1, totalCount + 1):
        distinctPrimeFactorsCount = 0  # Track the number of distinct prime factors
        workingNumber = currentNumber  # Store the original currentNumber for factorization

        # Step 3.1: Check for prime factors
        for potentialFactor in range(2, currentNumber):  # Check for factors starting from 2
            if workingNumber % potentialFactor == 0:  # If potentialFactor divides workingNumber
                distinctPrimeFactorsCount += 1  # Found a new distinct prime factor
                # Divide workingNumber until it is no longer divisible by potentialFactor
                while workingNumber % potentialFactor == 0:
                    workingNumber //= potentialFactor  # Remove all occurrences of this prime factor

            # If we already found two distinct prime factors, we can break early
            if distinctPrimeFactorsCount > 2:
                break

        # Step 3.2: Check if we have exactly two distinct prime factors
        if distinctPrimeFactorsCount == 2:
            countOfNumbersWithTwoDistinctPrimeFactors += 1  # Increment our result count

    # Step 4: Output the final result
    print(countOfNumbersWithTwoDistinctPrimeFactors)  # Print the count of numbers found

# Call the main function to execute the program
count_numbers_with_two_distinct_prime_factors()
