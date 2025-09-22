def main():
    # Step 2: Input an integer value 'n'
    n = int(input())

    # Step 3: Initialize a list 'isActive' of size 'n' with all elements set to True
    isActive = [True] * n

    # Step 4: Set Variables
    nextIndex = 0
    currentStep = 1

    # Step 5: Loop while 'currentStep' is less than or equal to 500,000
    while currentStep <= 500000:
        if isActive[nextIndex]:
            # Mark this index as inactive
            isActive[nextIndex] = False

        # Increment currentStep by 1
        currentStep += 1

        # Update nextIndex to wrap around within bounds
        nextIndex = (nextIndex + currentStep) % n

    # Step 6: Filter Active Elements
    activeElements = [index for index in range(n) if isActive[index]]

    # Step 7: Output results
    if len(activeElements) == 0:
        print("YES")
    else:
        print("NO")

# Step 1: Start the program
if __name__ == "__main__":
    main()
