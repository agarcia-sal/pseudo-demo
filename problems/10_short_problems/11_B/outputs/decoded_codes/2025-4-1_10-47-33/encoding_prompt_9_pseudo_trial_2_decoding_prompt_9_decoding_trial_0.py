# Get user input and convert it to an absolute integer value.
targetNumber = abs(int(input()))

# Initialize currentInteger to 0
currentInteger = 0

# Start an infinite loop
while True:
    # Calculate the sum of integers from 0 to currentInteger
    sumOfIntegers = currentInteger * (currentInteger + 1) // 2  # Using the formula for the sum of the first n integers
    
    # Calculate the difference between sumOfIntegers and targetNumber
    difference = sumOfIntegers - targetNumber
    
    # Check if sumOfIntegers is equal to targetNumber
    if sumOfIntegers == targetNumber:
        print(currentInteger)
        break  # Exit the loop
    
    # Check if sumOfIntegers is greater than targetNumber
    if sumOfIntegers > targetNumber:
        # If the difference is an even number
        if difference % 2 == 0:
            print(currentInteger)  # Print currentInteger
            break  # Exit the loop
    
    # Increment currentInteger by 1
    currentInteger += 1
