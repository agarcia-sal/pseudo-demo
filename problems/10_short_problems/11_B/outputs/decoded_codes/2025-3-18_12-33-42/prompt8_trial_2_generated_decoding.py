# Step 1: Read user input and take the absolute value
targetNumber = abs(int(input()))

# Step 2: Initialize currentIndex
currentIndex = 0

# Step 3: Infinite Loop
while True:
    # Step 4: Calculate Triangular Number
    triangularNumber = (currentIndex * (currentIndex + 1)) // 2
    
    # Step 5: Calculate Difference
    difference = triangularNumber - targetNumber
    
    # Step 6: Check Conditions
    if triangularNumber == targetNumber:
        print(currentIndex)  # Answer found
        break
    elif triangularNumber > targetNumber:
        if difference % 2 == 0:  # Check if difference is even
            print(currentIndex)  # Answer found
            break
    
    # Step 7: Increment Index
    currentIndex += 1
