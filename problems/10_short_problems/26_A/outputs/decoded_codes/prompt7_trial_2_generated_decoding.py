def countDistinctPrimeNumbers(t):
    # This will hold the count of numbers with exactly 2 distinct prime factors
    resultCount = 0

    # Iterate over each number from 1 to t
    for i in range(1, t + 1):
        # Counter for distinct prime factors of current number
        distinctPrimeCount = 0
        currentNumber = i  # Take the current number to analyze

        # Check for factors from 2 up to currentNumber - 1
        for j in range(2, currentNumber):
            if currentNumber % j == 0:  # Check if j is a factor of currentNumber
                distinctPrimeCount += 1  # We found a new distinct prime factor

                # Divide currentNumber by j until it's no longer divisible
                while currentNumber % j == 0:
                    currentNumber //= j  # Reduce currentNumber by factor j

        # Check if the number has exactly 2 distinct prime factors
        if distinctPrimeCount == 2:
            resultCount += 1  # We found a valid number

    return resultCount  # Return the total count of numbers with exactly 2 distinct prime factors


# Main execution
t = int(input())  # Get the upper limit from user
print(countDistinctPrimeNumbers(t))  # Call the function with input t and print the result
