# Start the Program

# Get User Input
targetValue = int(input())
targetValue = abs(targetValue)

# Initialize Variables
currentIndex = 0

# Begin Infinite Loop
while True:
    # Calculate the sum of the first 'currentIndex' integers
    sumOfIntegers = (currentIndex * (currentIndex + 1)) // 2
    
    # Calculate the difference
    difference = sumOfIntegers - targetValue
    
    # Check Conditions
    if sumOfIntegers == targetValue:
        print(currentIndex)  # Print the required number
        break
    
    if sumOfIntegers > targetValue:
        if difference % 2 == 0:  # Check if difference is evenly divisible by 2
            print(currentIndex)  # Print the required number
            break
    
    # Increment the currentIndex
    currentIndex += 1
