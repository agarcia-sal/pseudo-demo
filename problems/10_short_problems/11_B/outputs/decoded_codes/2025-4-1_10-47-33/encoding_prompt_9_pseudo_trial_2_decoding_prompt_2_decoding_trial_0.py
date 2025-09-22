# Step 1: Get the absolute value of user input
targetNumber = abs(int(input()))

# Step 2: Initialize currentInteger
currentInteger = 0

# Step 3: Start an infinite loop
while True:
    # Calculate sumOfIntegers
    sumOfIntegers = (currentInteger * (currentInteger + 1)) // 2  # Using the formula for the sum of the first n integers
    
    # Calculate difference
    difference = sumOfIntegers - targetNumber
    
    # Check if sumOfIntegers equals targetNumber
    if sumOfIntegers == targetNumber:
        print(currentInteger)
        break
    
    # Check if sumOfIntegers exceeds targetNumber
    if sumOfIntegers > targetNumber:
        # Check if the difference is even
        if difference % 2 == 0:
            print(currentInteger)
            break
    
    # Increment currentInteger
    currentInteger += 1
