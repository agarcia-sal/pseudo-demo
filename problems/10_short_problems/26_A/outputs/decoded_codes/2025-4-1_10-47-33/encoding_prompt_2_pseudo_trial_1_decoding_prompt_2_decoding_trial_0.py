# Input: Read an integer value t
t = int(input())

# Initialize a variable: Set resultCount to 0
resultCount = 0

# Iterate through potential candidates
for currentNumber in range(1, t + 1):
    # Initialize a counter: factorCount to 0
    factorCount = 0
    # Set currentValue to currentNumber
    currentValue = currentNumber

    # Check for factors
    for potentialFactor in range(2, currentNumber):
        # If currentValue is divisible by potentialFactor
        if currentValue % potentialFactor == 0:
            # Increment factorCount
            factorCount += 1
            # Remove all instances of potentialFactor from currentValue
            while currentValue % potentialFactor == 0:
                currentValue //= potentialFactor

    # Evaluate the condition
    if factorCount == 2:
        # Increment resultCount
        resultCount += 1

# Output: Display the total count of integers with exactly two distinct prime factors
print(resultCount)
