# Step 1: Start
# Step 2: Read an integer input 'timePeriod' 
timePeriod = int(input())

# Step 3: Initialize 'resultCount' to 0
resultCount = 0

# Step 4: For each integer 'currentNumber' from 1 to 'timePeriod' (inclusive):
for currentNumber in range(1, timePeriod + 1):
    # Step 4a: Initialize 'divisorCount' to 0
    divisorCount = 0
    
    # Step 4b: Set 'tempNumber' to 'currentNumber'
    tempNumber = currentNumber
    
    # Step 4c: For each integer 'potentialDivisor' from 2 to 'currentNumber' - 1:
    for potentialDivisor in range(2, currentNumber):
        # Step 4ci: If 'tempNumber' is divisible by 'potentialDivisor':
        if tempNumber % potentialDivisor == 0:
            # Step 4cA: Increment 'divisorCount' by 1
            divisorCount += 1
            
            # Step 4cB: While 'tempNumber' is divisible by 'potentialDivisor':
            while tempNumber % potentialDivisor == 0:
                # Step 4cBI: Divide 'tempNumber' by 'potentialDivisor'
                tempNumber //= potentialDivisor
    
    # Step 4d: If 'divisorCount' equals 2:
    if divisorCount == 2:
        # Step 4di: Increment 'resultCount' by 1
        resultCount += 1

# Step 5: Print 'resultCount'
print(resultCount)
# Step 6: End
