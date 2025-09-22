# Read the upper limit for checking integers
t = int(input())

# Initialize a counter for numbers with exactly two distinct prime factors
resultCount = 0

# Iterate through each number from 1 to t
for currentNumber in range(1, t + 1):
    # Counter for distinct prime factors
    factorCount = 0
    currentValue = currentNumber  # Value to manipulate for factor checking
    
    # Check for potential factors starting from 2 up to currentNumber - 1
    for potentialFactor in range(2, currentNumber):        
        if currentValue % potentialFactor == 0:  # potentialFactor is a factor
            factorCount += 1  # Found a new distinct prime factor
            
            # Continuously divide out all instances of this factor
            while currentValue % potentialFactor == 0:  
                currentValue //= potentialFactor
    
    # After checking for factors, evaluate if the count is exactly 2
    if factorCount == 2:
        resultCount += 1  # Found a number with exactly two distinct prime factors

# Output the total count of such numbers
print(resultCount)
