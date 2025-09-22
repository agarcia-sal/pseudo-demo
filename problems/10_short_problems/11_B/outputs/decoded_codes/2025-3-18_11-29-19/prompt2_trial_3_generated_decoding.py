# 1. Begin the program.

# 2. Prompt the user for input and store the absolute value of the integer input as targetValue.
targetValue = abs(int(input()))

# 3. Initialize a counter variable index to 0.
index = 0

# 4. Start an indefinite loop to continue processing until a specific condition is met.
while True:
    # 1. Calculate the sum currentSum of the first index natural numbers.
    currentSum = (index * (index + 1)) / 2
    
    # 2. Calculate difference as currentSum - targetValue.
    difference = currentSum - targetValue
    
    # 3. Check if currentSum is equal to targetValue.
    if currentSum == targetValue:
        # a. If they are equal, print the current value of index and exit the loop.
        print(index)
        break

    # 4. Check if currentSum is greater than targetValue.
    if currentSum > targetValue:
        # a. If it is, check if difference is an even number.
        if difference % 2 == 0:
            # i. If difference is even, print the current value of index and exit the loop.
            print(index)
            break
            
    # 5. Increment the value of index by 1.
    index += 1

# 5. End the program.
