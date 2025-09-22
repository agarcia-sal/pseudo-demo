def main():
    # Step 1: Input Handling
    numberOfElements = int(input())
    
    # Step 2: Initialization
    statusList = [True] * numberOfElements  # List of True values
    currentIndex = 0
    stepIncrement = 1

    # Step 3: Looping Process
    while stepIncrement <= 500000:
        if statusList[currentIndex]:  # Check if the current index is True
            statusList[currentIndex] = False  # Set to False if True
        stepIncrement += 1  # Increment step
        currentIndex = (currentIndex + stepIncrement) % numberOfElements  # Update index with wrap-around
        
    # Step 4: Filtering Results
    trueValues = [status for status in statusList if status]  # Collect all True values

    # Step 5: Output Handling
    if len(trueValues) == 0:
        print("YES")  # If no True values left
    else:
        print("NO")  # If there are still True values

# Start of the program
if __name__ == "__main__":
    main()
