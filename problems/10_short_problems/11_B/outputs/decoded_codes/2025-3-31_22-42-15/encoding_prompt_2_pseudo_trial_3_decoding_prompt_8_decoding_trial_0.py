# Step 1: Input
targetValue = abs(int(input()))

# Step 2: Initialization
index = 0

# Step 3: Loop
while True:
    # Step 3a: Calculate currentSum
    currentSum = (index * (index + 1)) // 2

    # Step 3b: Compute difference
    difference = currentSum - targetValue

    # Step 3c: Check if currentSum equals targetValue
    if currentSum == targetValue:
        print(index)
        break

    # Step 3d: Check if currentSum is greater than targetValue
    if currentSum > targetValue and difference % 2 == 0:
        print(index)
        break
    
    # Step 3e: Increment index
    index += 1
