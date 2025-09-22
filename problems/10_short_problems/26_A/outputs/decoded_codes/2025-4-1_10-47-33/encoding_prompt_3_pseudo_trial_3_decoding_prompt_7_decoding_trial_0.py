# Begin of the program

# Read the number of test cases or range limit
testCaseCount = int(input())

# Initialize a variable to hold the result count
resultCount = 0

# Loop through each number from 1 to the test case count (inclusive)
for number in range(1, testCaseCount + 1):
    
    # Initialize a counter for the number of distinct prime factors
    distinctPrimeFactorCount = 0
    
    # Create a variable to hold the current number to be checked
    currentNumber = number

    # Loop through potential factors starting from 2 up to one less than the number
    for potentialFactor in range(2, number):
        
        # Check if the potential factor divides the current number evenly
        if currentNumber % potentialFactor == 0:
            
            # Increase the count of distinct prime factors
            distinctPrimeFactorCount += 1
            
            # Divide the current number by the factor as long as it's divisible
            while currentNumber % potentialFactor == 0:
                currentNumber //= potentialFactor
            
        # Optional: If we already found two distinct prime factors, no need to check further
        if distinctPrimeFactorCount > 2:
            break
            
    # Check if the current number has exactly two distinct prime factors
    if distinctPrimeFactorCount == 2:
        # Increment the result count for numbers with precisely two distinct prime factors
        resultCount += 1

# Output the total count of numbers with exactly two distinct prime factors
print(resultCount)

# End of the program
