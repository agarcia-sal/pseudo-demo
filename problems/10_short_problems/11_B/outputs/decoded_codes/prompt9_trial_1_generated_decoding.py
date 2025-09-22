# Receive input from the user and ensure it's processed as an integer
targetValue = int(input())
# Calculate the absolute value of the targetValue
targetValue = abs(targetValue)

# Initialize the current index
currentIndex = 0

# Start an infinite loop to find the required index
while True:
    # Calculate the sum of the first currentIndex integers
    sumOfIntegers = currentIndex * (currentIndex + 1) // 2
    # Calculate the difference between sumOfIntegers and targetValue
    difference = sumOfIntegers - targetValue
    
    # Check if the sum equals the targetValue
    if sumOfIntegers == targetValue:
        print(currentIndex)
        break
    # Check if the sum is greater than targetValue
    elif sumOfIntegers > targetValue:
        # If the difference is even, we can achieve balance
        if difference % 2 == 0:
            print(currentIndex)
            break
    
    # Increment currentIndex to check the next integer
    currentIndex += 1
