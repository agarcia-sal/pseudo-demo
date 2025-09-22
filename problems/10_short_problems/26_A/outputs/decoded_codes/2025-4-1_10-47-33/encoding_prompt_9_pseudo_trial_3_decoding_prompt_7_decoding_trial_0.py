# Start the program and read an integer t from the user
t = int(input())

# Initialize a count variable to keep track of semiprime numbers found
semiprimeCount = 0

# Loop through each number from 1 to t (inclusive)
for currentNumber in range(1, t + 1):
    # Set a counter for distinct prime factors
    distinctPrimeCount = 0
    # Set a variable to find prime factors
    number = currentNumber
    
    # Loop through potential factors starting from 2 up to currentNumber - 1
    for potentialFactor in range(2, currentNumber):
        # Check if the current number is divisible by the potential factor
        if number % potentialFactor == 0:
            # Increase distinct prime count
            distinctPrimeCount += 1
            
            # While the current number is divisible by potentialFactor
            while number % potentialFactor == 0:
                # Divide number by potentialFactor
                number //= potentialFactor
    
    # After checking all potential factors
    # If distinctPrimeCount is equal to 2, we've found a semiprime
    if distinctPrimeCount == 2:
        semiprimeCount += 1  # Increase semiprime count

# Once all numbers have been checked, output the semiprime count
print(semiprimeCount)
