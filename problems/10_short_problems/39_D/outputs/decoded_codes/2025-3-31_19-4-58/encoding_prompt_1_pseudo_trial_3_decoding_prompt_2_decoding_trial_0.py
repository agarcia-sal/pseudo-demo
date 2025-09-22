def mainProcedure():
    # Get two strings as input
    firstInput = input()
    secondInput = input()

    # Split the input strings into lists based on spaces
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize differenceCount to 0
    differenceCount = 0

    # Compare each element in the lists
    for index in range(3):  # Assuming there are at least 3 elements
        # Convert the current elements to integers
        firstElement = int(firstList[index])
        secondElement = int(secondList[index])

        # Check if the elements are different
        if firstElement != secondElement:
            differenceCount += 1

    # Check the number of differences
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the mainProcedure function
mainProcedure()
