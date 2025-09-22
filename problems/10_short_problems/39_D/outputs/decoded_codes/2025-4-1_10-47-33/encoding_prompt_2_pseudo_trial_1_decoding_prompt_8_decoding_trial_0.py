def main():
    # Receive Input
    firstList = input()
    secondList = input()

    # Split Input into Lists
    firstElements = firstList.split()
    secondElements = secondList.split()

    # Initialize a Counter
    differenceCount = 0

    # Compare Corresponding Elements
    for index in range(3):
        currentFirstValue = int(firstElements[index])
        currentSecondValue = int(secondElements[index])
        if currentFirstValue != currentSecondValue:
            differenceCount += 1

    # Check Number of Differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Invoke Main Function to Begin Execution
main()
