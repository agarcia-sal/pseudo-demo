# Begin
absoluteValue = abs(int(input()))  # Declare absoluteValue as the absolute value of user input
currentIndex = 0  # Initialize currentIndex to 0

# Start an indefinite loop
while True:
    # Calculate sumOfNumbers using the formula
    sumOfNumbers = (currentIndex * (currentIndex + 1)) // 2  # Use integer division

    # Calculate the difference
    difference = sumOfNumbers - absoluteValue

    # Check if sumOfNumbers equals absoluteValue
    if sumOfNumbers == absoluteValue:
        print(currentIndex)  # Print currentIndex
        break  # Exit the loop

    # Check if sumOfNumbers is greater than absoluteValue
    elif sumOfNumbers > absoluteValue:
        # If difference is even
        if difference % 2 == 0:
            print(currentIndex)  # Print currentIndex
            break  # Exit the loop

    # Increment currentIndex
    currentIndex += 1

# End
