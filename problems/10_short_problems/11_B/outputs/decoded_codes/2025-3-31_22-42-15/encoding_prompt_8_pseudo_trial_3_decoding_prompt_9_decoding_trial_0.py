# Start the Program

# Get User Input
targetValue = int(input())  # Read an integer value from the user
absoluteValue = abs(targetValue)  # Calculate the absolute value of targetValue

# Initialize Variables
currentIndex = 0  # Set a counter variable to 0

# Begin Infinite Loop
while True:
    # Calculate the sum of the first 'currentIndex' integers
    sumOfIntegers = (currentIndex * (currentIndex + 1)) // 2  # Using integer division

    # Calculate the difference
    difference = sumOfIntegers - absoluteValue

    # Check Conditions
    if sumOfIntegers == absoluteValue:
        print(currentIndex)  # Print currentIndex if it matches the target
        break  # Exit the loop
    if sumOfIntegers > absoluteValue:
        if difference % 2 == 0:  # Check if the difference is evenly divisible by 2
            print(currentIndex)  # Print currentIndex if the condition is met
            break  # Exit the loop

    # Increment currentIndex for the next iteration
    currentIndex += 1
