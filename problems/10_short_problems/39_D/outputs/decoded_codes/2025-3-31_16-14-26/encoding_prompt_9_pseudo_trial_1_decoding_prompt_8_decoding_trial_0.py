def main():
    # Receive Input
    first_input = input()
    second_input = input()

    # Split Input into Individual Numbers
    firstSet = list(map(int, first_input.split()))
    secondSet = list(map(int, second_input.split()))

    # Initialize Difference Counter
    differenceCount = 0

    # Compare Corresponding Items
    for i in range(3):
        firstNumber = firstSet[i]
        secondNumber = secondSet[i]
        if firstNumber != secondNumber:
            differenceCount += 1

    # Determine Result Based on Differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execution Trigger
if __name__ == "__main__":
    main()
