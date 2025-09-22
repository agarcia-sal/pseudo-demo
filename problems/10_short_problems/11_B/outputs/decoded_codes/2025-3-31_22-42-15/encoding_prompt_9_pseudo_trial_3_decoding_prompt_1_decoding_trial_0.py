# Step 1: Get Input
targetSum = abs(int(input()))

# Step 2: Initialize a Counter
currentIndex = 0

# Step 3: Loop for Calculation
while True:
    # Calculate the sum of the first currentIndex integers
    currentSum = (currentIndex * (currentIndex + 1)) // 2  # Using // for integer division
    
    # Calculate the difference
    difference = currentSum - targetSum
    
    # Check Conditions
    if currentSum == targetSum:
        print(currentIndex)
        break  # Stop the process
    elif currentSum > targetSum:
        if difference % 2 == 0:  # Check if the difference is even
            print(currentIndex)
            break  # Stop the process
            
    # Increment currentIndex by 1
    currentIndex += 1
