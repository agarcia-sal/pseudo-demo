# Start the Program

# Get User Input
targetValue = int(input())  # Read an integer value from the user
targetValue = abs(targetValue)  # Calculate the absolute value of targetValue

# Initialize Variables
currentIndex = 0  # Set a counter variable to track the current index

# Begin Infinite Loop
while True:
    # Calculate the sum of the first 'currentIndex' integers
    sumOfIntegers = (currentIndex * (currentIndex + 1)) // 2  # Using integer division
    
    # Calculate the difference between sumOfIntegers and targetValue
    difference = sumOfIntegers - targetValue
    
    # Check Conditions
    if sumOfIntegers == targetValue:
        print(currentIndex)  # Print currentIndex when the sum matches targetValue
        break  # Exit the loop
    elif sumOfIntegers > targetValue:
        # Check if the difference is evenly divisible by 2
        if difference % 2 == 0:
            print(currentIndex)  # Print currentIndex when the condition is satisfied
            break  # Exit the loop
    
    # Increment currentIndex by 1 to check the next integer in the next iteration
    currentIndex += 1
