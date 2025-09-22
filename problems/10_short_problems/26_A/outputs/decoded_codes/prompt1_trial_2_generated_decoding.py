# Step 1: Read an integer value t from the user input
t = int(input())

# Step 2: Initialize a variable result to 0
result = 0

# Step 3: For each integer currentNumber from 1 to t (inclusive)
for currentNumber in range(1, t + 1):
    # Step 3.1: Initialize a counter divisorCount to 0
    divisorCount = 0
    # Step 3.2: Set a variable value equal to currentNumber
    value = currentNumber
    
    # Step 3.3: For each integer potentialDivisor from 2 to currentNumber - 1
    for potentialDivisor in range(2, currentNumber):
        # Step 3.3.1: If value is divisible by potentialDivisor
        if value % potentialDivisor == 0:
            # Step 3.3.1.1: Increment divisorCount by 1
            divisorCount += 1
            # Step 3.3.1.2: While value is still divisible by potentialDivisor
            while value % potentialDivisor == 0:
                # Step 3.3.1.2.1: Divide value by potentialDivisor
                value //= potentialDivisor

    # Step 3.4: If divisorCount equals 2
    if divisorCount == 2:
        # Step 3.4.1: Increment result by 1
        result += 1

# Step 4: After checking all numbers up to t, output the final count stored in result
print(result)
