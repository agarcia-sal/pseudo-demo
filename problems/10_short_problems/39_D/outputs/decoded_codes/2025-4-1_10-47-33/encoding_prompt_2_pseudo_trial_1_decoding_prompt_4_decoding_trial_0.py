def main():
    # Step 1: Receive Input
    firstList = input()
    secondList = input()

    # Step 2: Split Input into Lists
    firstElements = firstList.split()
    secondElements = secondList.split()

    # Step 3: Initialize a Counter
    differenceCount = 0

    # Step 4: Compare Corresponding Elements
    for index in range(3):  # We assume that the input will have at least 3 elements
        currentFirstValue = int(firstElements[index])
        currentSecondValue = int(secondElements[index])
        if currentFirstValue != currentSecondValue:
            differenceCount += 1

    # Step 5: Check Number of Differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Step 6: Invoke Main Function to Begin Execution
if __name__ == "__main__":
    main()
