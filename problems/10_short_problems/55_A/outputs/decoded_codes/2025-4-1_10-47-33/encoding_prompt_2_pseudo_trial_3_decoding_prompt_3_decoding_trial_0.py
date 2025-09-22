def main():
    # Input Handling
    numberOfElements = int(input())  # Read an integer value from user

    # Initialization
    statusList = [True] * numberOfElements  # Initialize all values to True
    currentIndex = 0
    stepIncrement = 1

    # Looping Process
    while stepIncrement <= 500000:
        if statusList[currentIndex]:  # Check the value at the current index
            statusList[currentIndex] = False  # Set the value to False

        stepIncrement += 1  # Increment step count
        currentIndex = (currentIndex + stepIncrement) % numberOfElements  # Update index with wrap-around

    # Filtering Results
    trueValues = [value for value in statusList if value]  # Get all True values

    # Output Handling
    if len(trueValues) == 0:
        print("YES")  # Output if no True values are left
    else:
        print("NO")   # Output if there are still True values

# Call the main function to execute the program
main()
