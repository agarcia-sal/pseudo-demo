# BEGIN

# Read the input value
inputNumber = int(input())

# Initialize a variable to count the desired numbers
countOfNumbers = 0

# Loop through each number from 1 to inputNumber
for currentNumber in range(1, inputNumber + 1):
    
    # Initialize a counter to track the number of distinct prime factors
    distinctPrimeCount = 0
    
    # Create a variable to work with currentNumber
    workingNumber = currentNumber
    
    # Check for prime factors starting from 2 up to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        
        # If potentialFactor is a factor of workingNumber
        if workingNumber % potentialFactor == 0:
            
            # Increase the count of distinct prime factors
            distinctPrimeCount += 1
            
            # Divide workingNumber by potentialFactor until it is no longer divisible
            while workingNumber % potentialFactor == 0:
                workingNumber //= potentialFactor

    # Check if the number has exactly two distinct prime factors
    if distinctPrimeCount == 2:
        
        # Increase the overall count of such numbers
        countOfNumbers += 1

# Output the result, which is the count of numbers with exactly two distinct prime factors
print(countOfNumbers)

# END
