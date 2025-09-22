# Start the Program

# Get User Input
targetValue = int(input())       # Read an integer value from the user
targetValue = abs(targetValue)   # Calculate the absolute value of targetValue

# Initialize Variables
currentIndex = 0                 # Set a counter variable to 0

# Begin Infinite Loop
while True:
    # Calculate the sum of the first 'currentIndex' integers
    sumOfIntegers = (currentIndex * (currentIndex + 1)) / 2
    
    # Calculate the difference between sumOfIntegers and targetValue
    difference = sumOfIntegers - targetValue
    
    # Check Conditions
    if sumOfIntegers == targetValue:
        print(currentIndex)       # Print currentIndex
        break                     # Exit the loop
    elif sumOfIntegers > targetValue:
        if difference % 2 == 0:   # Check if difference is evenly divisible by 2
            print(currentIndex)   # Print currentIndex
            break                 # Exit the loop
    
    # Increment currentIndex by 1
    currentIndex += 1
