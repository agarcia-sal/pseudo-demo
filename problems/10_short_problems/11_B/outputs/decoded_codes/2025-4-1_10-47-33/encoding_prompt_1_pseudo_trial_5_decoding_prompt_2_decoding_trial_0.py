# 1. Input: Read an integer and calculate the absolute value
targetNumber = abs(int(input()))

# 2. Initialize: Set the counter variable index to 0
index = 0

# 3. Loop: Start an infinite loop
while True:
    # Calculate the sum of the first index natural numbers
    currentSum = index * (index + 1) // 2  # Use // for integer division

    # Calculate the difference between currentSum and targetNumber
    difference = currentSum - targetNumber
    
    # Check Conditions
    if currentSum == targetNumber:
        print(index)
        break  # Exit the loop
    elif currentSum > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(index)
            break  # Exit the loop

    # Increment the value of index by 1
    index += 1
