# This algorithm finds the smallest non-negative integer whose cumulative sum 
# of the first 'i' natural numbers either equals a given non-negative integer 
# or exceeds it by an even number.

# Step 1: Get user input and convert to absolute integer value
targetNumber = abs(int(input()))

# Step 2: Initialize currentInteger to 0
currentInteger = 0

# Step 3: Start an infinite loop to find the correct integer
while True:
    # Calculate sumOfIntegers using the formula for the sum of the first n integers
    sumOfIntegers = (currentInteger * (currentInteger + 1)) // 2
    
    # Calculate the difference between sumOfIntegers and targetNumber
    difference = sumOfIntegers - targetNumber
    
    # Check if sumOfIntegers equals targetNumber
    if sumOfIntegers == targetNumber:
        print(currentInteger)  # Output the currentInteger
        break  # Exit the loop
    
    # Check if sumOfIntegers exceeds targetNumber
    if sumOfIntegers > targetNumber:
        # Check if the difference is an even number
        if difference % 2 == 0:
            print(currentInteger)  # Output the currentInteger
            break  # Exit the loop
    
    # Increment currentInteger by 1 for the next iteration
    currentInteger += 1
