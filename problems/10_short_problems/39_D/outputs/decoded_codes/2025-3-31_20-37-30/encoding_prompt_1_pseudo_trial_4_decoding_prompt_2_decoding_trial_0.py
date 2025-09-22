def main():
    # Receive Input
    firstInput = input()
    secondInput = input()

    # Split Inputs
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize Difference Counter
    differenceCount = 0

    # Compare Corresponding Elements
    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        if firstValue != secondValue:
            differenceCount += 1

    # Determine Output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute Main Function
if __name__ == "__main__":
    main()
