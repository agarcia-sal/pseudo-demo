# Step 1: Receive Input
targetNumber = abs(int(input()))

# Step 2: Initialize Counter
currentIndex = 0

# Step 3: Iterative Search
while True:
    # Calculate sumOfFirstN
    sumOfFirstN = (currentIndex * (currentIndex + 1)) // 2
    
    # Determine difference
    difference = sumOfFirstN - targetNumber

    # Check Conditions
    if sumOfFirstN == targetNumber:
        print(currentIndex)
        break
    elif sumOfFirstN > targetNumber:
        if difference % 2 == 0:
            print(currentIndex)
            break
    
    # Increment counter
    currentIndex += 1
