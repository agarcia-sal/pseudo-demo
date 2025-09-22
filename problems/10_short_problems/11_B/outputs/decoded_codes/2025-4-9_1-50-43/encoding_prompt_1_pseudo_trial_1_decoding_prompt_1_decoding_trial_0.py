# Step 1: Get User Input
targetValue = abs(int(input()))

# Step 2: Initialize Counter
currentIndex = 0

# Step 3: Begin Infinite Loop
while True:
    # Step 3a: Calculate Sum of First n Integers
    sumOfIntegers = (currentIndex * (currentIndex + 1)) // 2

    # Step 3b: Determine Difference
    difference = sumOfIntegers - targetValue

    # Step 3c: Check for Conditions
    if sumOfIntegers == targetValue:
        print(currentIndex)
        break
    elif sumOfIntegers > targetValue:
        if difference % 2 == 0:
            print(currentIndex)
            break

    # Step 3d: Increment Counter
    currentIndex += 1
