# 1. Start (implicit in the main program)
# 2. Read an integer input 'timePeriod'
timePeriod = int(input())
# 3. Initialize 'resultCount' to 0
resultCount = 0
# 4. For each integer 'currentNumber' from 1 to 'timePeriod' (inclusive):
for currentNumber in range(1, timePeriod + 1):
    # a. Initialize 'divisorCount' to 0
    divisorCount = 0
    # b. Set 'tempNumber' to 'currentNumber'
    tempNumber = currentNumber
    # c. For each integer 'potentialDivisor' from 2 to 'currentNumber' - 1:
    for potentialDivisor in range(2, currentNumber):
        # i. If 'tempNumber' is divisible by 'potentialDivisor':
        if tempNumber % potentialDivisor == 0:
            # A. Increment 'divisorCount' by 1
            divisorCount += 1
            # B. While 'tempNumber' is divisible by 'potentialDivisor':
            while tempNumber % potentialDivisor == 0:
                # I. Divide 'tempNumber' by 'potentialDivisor'
                tempNumber //= potentialDivisor
    # d. If 'divisorCount' equals 2:
    if divisorCount == 2:
        # i. Increment 'resultCount' by 1
        resultCount += 1
# 5. Print 'resultCount'
print(resultCount)
# 6. End (implicit in the end of the program)
