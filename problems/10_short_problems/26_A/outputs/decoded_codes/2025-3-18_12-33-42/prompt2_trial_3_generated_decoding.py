# Step 1: Accept an integer input named "t" which indicates the upper limit
t = int(input())

# Step 2: Initialize a variable "result" to zero
result = 0

# Step 3: Loop through each integer "currentNumber" from 1 to "t" (inclusive)
for currentNumber in range(1, t + 1):
    
    # Step 4: Initialize a counter "divisorCount" to zero
    divisorCount = 0
    
    # Step 5: Set a variable "temp" equal to "currentNumber"
    temp = currentNumber
    
    # Step 6: Loop through each integer "potentialDivisor" from 2 to currentNumber - 1
    for potentialDivisor in range(2, currentNumber):
        
        # Step 7: Check if "temp" is divisible by "potentialDivisor"
        if temp % potentialDivisor == 0:
            # Step 7.1: Increment "divisorCount" by one
            divisorCount += 1
            
            # Step 8: Remove all instances of this factor from "temp"
            while temp % potentialDivisor == 0:
                temp //= potentialDivisor
    
    # Step 9: After checking all potential divisors, evaluate if "divisorCount" equals 2
    if divisorCount == 2:
        # Step 9.1: Increment the "result" by one
        result += 1

# Step 10: Output the final value of "result"
print(result)
