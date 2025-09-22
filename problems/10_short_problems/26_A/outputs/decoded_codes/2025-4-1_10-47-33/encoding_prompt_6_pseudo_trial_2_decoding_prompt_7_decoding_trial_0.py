# Step 1: Start by reading an integer input called "totalNumbers".
totalNumbers = int(input())

# Step 2: Initialize a variable "countOfSpecialNumbers" to 0. This variable will store the final result.
countOfSpecialNumbers = 0

# Step 3: Loop through each integer "currentNumber" from 1 to "totalNumbers" (inclusive).
for currentNumber in range(1, totalNumbers + 1):
    # Step 3a: Initialize a variable "divisorCount" to 0 to keep track of the number of unique divisors for the current number.
    divisorCount = 0
    # Step 3b: Set "currentValue" to "currentNumber".
    currentValue = currentNumber

    # Step 3c: Loop through each integer "divisor" from 2 to "currentNumber - 1".
    for divisor in range(2, currentNumber):
        # Step 3c.i: If "currentValue" is divisible by "divisor".
        if currentValue % divisor == 0:
            # Increment "divisorCount" by 1.
            divisorCount += 1
            
            # Step 3c.ii: While "currentValue" is still divisible by "divisor".
            while currentValue % divisor == 0:
                # Divide "currentValue" by "divisor".
                currentValue //= divisor  # This removes all instances of this divisor from "currentValue".

    # Step 3d: If "divisorCount" is equal to 2.
    if divisorCount == 2:
        # Increment "countOfSpecialNumbers" by 1.
        countOfSpecialNumbers += 1

# Step 4: After checking all numbers, print "countOfSpecialNumbers".
print(countOfSpecialNumbers)

# Step 5: End of the program.
