def doMain():
    # Prompt for User Input
    inputString1 = input()
    inputString2 = input()

    # Process the Input
    listOfValues1 = inputString1.split()
    listOfValues2 = inputString2.split()

    # Initialize a Counter
    differenceCount = 0

    # Compare Values
    for index in range(3):  # iterate through indices 0 to 2
        valueA = int(listOfValues1[index])
        valueB = int(listOfValues2[index])
        if valueA != valueB:
            differenceCount += 1

    # Output the Result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start the Program
if __name__ == "__main__":
    doMain()
