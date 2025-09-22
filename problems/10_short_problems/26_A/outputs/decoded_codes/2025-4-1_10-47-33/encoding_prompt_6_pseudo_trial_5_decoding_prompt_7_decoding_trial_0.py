# Function to count numbers with exactly two distinct prime factors
def count_numbers_with_two_distinct_prime_factors():
    # Step 1: Read an integer 't' as the upper limit
    t = int(input())
    
    # Step 2: Initialize total count of numbers with exactly two distinct prime factors
    totalCount = 0

    # Step 3: Loop through each number from 1 to 't'
    for currentNumber in range(1, t + 1):
        distinctPrimeCount = 0  # To track distinct prime factors
        currentValue = currentNumber  # Store the current number for factorization

        # Step 4: Find prime factors
        for potentialPrime in range(2, currentNumber):  # Check potential primes
            if currentValue % potentialPrime == 0:  # Check divisibility
                distinctPrimeCount += 1  # Found a new distinct prime factor
                
                # Remove all occurrences of potentialPrime from currentValue
                while currentValue % potentialPrime == 0:
                    currentValue //= potentialPrime
                
        # Step 5: Check if the count of distinct primes is exactly 2
        if distinctPrimeCount == 2:
            totalCount += 1  # Increment the count if there are exactly two distinct primes

    # Step 6: Output the result
    print(totalCount)  # Print the total count

# Call the function to execute the process
count_numbers_with_two_distinct_prime_factors()
