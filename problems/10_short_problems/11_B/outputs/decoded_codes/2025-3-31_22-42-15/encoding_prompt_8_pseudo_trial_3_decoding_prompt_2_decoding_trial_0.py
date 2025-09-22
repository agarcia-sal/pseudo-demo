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
        break  # Exit the loop
    if sumOfIntegers > targetValue:
        if difference % 2 == 0:  # Check if the difference is evenly divisible by 2
            print(currentIndex)  # Print the required number
            break  # Exit the loop
    
    # Increment currentIndex by 1
    currentIndex += 1
