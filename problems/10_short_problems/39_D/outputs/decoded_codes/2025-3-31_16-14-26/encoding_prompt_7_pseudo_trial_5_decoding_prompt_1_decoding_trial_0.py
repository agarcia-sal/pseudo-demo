def MainFunction():
    # Prompt the user for input
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists of substrings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Compare corresponding elements in the two lists
    for index in range(3):
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the values differ
        if firstValue != secondValue:
            differenceCount += 1 

    # Determine the output based on the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Initiates the MainFunction when the script is executed
if __name__ == "__main__":
    MainFunction()
