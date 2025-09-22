def mainProcedure():
    # Read the first list of integers as a string
    firstInput = input()
    
    # Read the second list of integers as a string
    secondInput = input()
    
    # Split the input strings into lists of integers
    firstList = list(map(int, firstInput.split()))
    secondList = list(map(int, secondInput.split()))
    
    # Initialize a counter for differences
    differenceCount = 0 

    # Compare the integers in the two lists
    for index in range(3):  # Assuming the lists will always have exactly 3 elements
        firstValue = firstList[index]
        secondValue = secondList[index]

        # If the values differ, increase the difference count
        if firstValue != secondValue:
            differenceCount += 1

    # Check the count of differences to determine the output
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Execute the main procedure
mainProcedure()
