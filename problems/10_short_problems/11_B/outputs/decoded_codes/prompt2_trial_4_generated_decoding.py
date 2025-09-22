# 1. Start the process.
# 2. Input a number called `userInput`.
userInput = input()

# 3. Convert `userInput` to an integer and take its absolute value, storing it in `targetNumber`.
targetNumber = abs(int(userInput))

# 4. Initialize a variable `currentIndex` to 0.
currentIndex = 0

# 5. Repeat indefinitely (loop):
while True:
    # 1. Calculate the sum `sumOfFirstN` as the sum of all integers from 0 to `currentIndex`.
    sumOfFirstN = (currentIndex * (currentIndex + 1)) // 2  # Sum of first N integers formula
    
    # 2. Determine `difference` by subtracting `targetNumber` from `sumOfFirstN`.
    difference = sumOfFirstN - targetNumber
    
    # 3. If `sumOfFirstN` equals `targetNumber`, then:
    if sumOfFirstN == targetNumber:
        # Output `currentIndex`.
        print(currentIndex)
        # Exit the loop.
        break
    
    # 4. Else if `sumOfFirstN` is greater than `targetNumber`, then:
    elif sumOfFirstN > targetNumber:
        # If `difference` is an even number, then:
        if difference % 2 == 0:
            # Output `currentIndex`.
            print(currentIndex)
            # Exit the loop.
            break
    
    # 5. Increment `currentIndex` by 1.
    currentIndex += 1

# 6. End the process.
