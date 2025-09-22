# Step 1: Obtain a positive integer from the user
targetValue = abs(int(input()))

# Step 2: Initialize currentIndex
currentIndex = 0

# Step 3: Begin an infinite loop to calculate triangular numbers
while True:
    # Step 3a: Calculate the triangular number
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2
    
    # Step 3b: Calculate the difference
    difference = triangularNumber - targetValue
    
    # Step 3c: Check if triangular number equals targetValue
    if triangularNumber == targetValue:
        print(currentIndex)
        break
    
    # Step 3d: Check if triangular number is greater than targetValue
    if triangularNumber > targetValue:
        # Check if difference is even
        if difference % 2 == 0:
            print(currentIndex)
            break
    
    # Step 3e: Increment currentIndex
    currentIndex += 1
