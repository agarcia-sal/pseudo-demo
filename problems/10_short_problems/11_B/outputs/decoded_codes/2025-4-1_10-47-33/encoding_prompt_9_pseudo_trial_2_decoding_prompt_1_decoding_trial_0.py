# Step 1: Get the absolute value of user input and assign it to targetNumber.
targetNumber = abs(int(input()))

# Step 2: Initialize currentInteger to 0.
currentInteger = 0

# Step 3: Start an infinite loop.
while True:
    # Step 4: Calculate sumOfIntegers as the sum of all integers from 0 to currentInteger.
    sumOfIntegers = currentInteger * (currentInteger + 1) // 2  # Using the formula n * (n + 1) / 2
    
    # Step 5: Calculate difference as the difference between sumOfIntegers and targetNumber.
    difference = sumOfIntegers - targetNumber
    
    # Step 6: Check if sumOfIntegers is equal to targetNumber
    if sumOfIntegers == targetNumber:
        # Output currentInteger and stop the loop.
        print(currentInteger)
        break
    
    # Step 7: Check if sumOfIntegers is greater than targetNumber
    if sumOfIntegers > targetNumber:
        # Step 8: Check if the difference is even
        if difference % 2 == 0:
            # Output currentInteger and stop the loop.
            print(currentInteger)
            break
    
    # Step 9: Increment currentInteger by 1.
    currentInteger += 1
