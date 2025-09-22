# Input the number of test cases
numberOfTestCases = int(input())

# Initialize the result variable
countOfSpecialNumbers = 0

# Loop through each number from 1 to numberOfTestCases
for currentNumber in range(1, numberOfTestCases + 1):
    divisorCount = 0
    tempNumber = currentNumber

    # Determine the factors of currentNumber
    for potentialDivisor in range(2, currentNumber):
        if tempNumber % potentialDivisor == 0:
            divisorCount += 1
            while tempNumber % potentialDivisor == 0:
                tempNumber //= potentialDivisor

    # Check if currentNumber has exactly two unique prime factors
    if divisorCount == 2:
        countOfSpecialNumbers += 1

# Output the result
print(countOfSpecialNumbers)
