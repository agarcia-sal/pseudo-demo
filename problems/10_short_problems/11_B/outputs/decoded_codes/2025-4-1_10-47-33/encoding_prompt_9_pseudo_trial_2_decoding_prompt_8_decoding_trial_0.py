# Step 1: Get the absolute value of the user input.
targetNumber = abs(int(input()))

# Step 2: Initialize currentInteger to 0.
currentInteger = 0

# Step 3: Start an infinite loop.
while True:
    # Calculate sumOfIntegers using the formula for the sum of the first 'currentInteger' integers.
    sumOfIntegers = (currentInteger * (currentInteger + 1)) // 2
    
    # Calculate the difference.
    difference = sumOfIntegers - targetNumber
    
    # Check if sumOfIntegers is equal to targetNumber.
    if sumOfIntegers == targetNumber:
        print(currentInteger)
        break
    
    # Check if sumOfIntegers exceeds targetNumber.
    if sumOfIntegers > targetNumber:
        # Check if the difference is an even number.
        if difference % 2 == 0:
            print(currentInteger)
            break
    
    # Increment currentInteger by 1.
    currentInteger += 1
