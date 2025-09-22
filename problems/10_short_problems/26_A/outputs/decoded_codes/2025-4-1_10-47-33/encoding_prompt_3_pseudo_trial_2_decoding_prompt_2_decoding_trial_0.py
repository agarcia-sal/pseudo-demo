# Get the number of test cases from user input
testCaseCount = int(input())

# Initialize a result variable to store count of prime numbers
primeCount = 0

# Loop over each number from 1 to the value of testCaseCount
for currentNumber in range(1, testCaseCount + 1):

    # Initialize a counter to track factors
    factorCount = 0
    
    # Set tempNumber to current number for factorization
    tempNumber = currentNumber
    
    # Loop over possible factors from 2 to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        
        # Check if potentialFactor divides tempNumber
        if tempNumber % potentialFactor == 0:
            # If it is a factor, increment the counter
            factorCount += 1
            
            # Continuously divide tempNumber by potentialFactor
            while tempNumber % potentialFactor == 0:
                tempNumber //= potentialFactor
            
    # If exactly two distinct factors were found, it is a prime number
    if factorCount == 2:
        primeCount += 1

# Output the count of prime numbers found
print(primeCount)
