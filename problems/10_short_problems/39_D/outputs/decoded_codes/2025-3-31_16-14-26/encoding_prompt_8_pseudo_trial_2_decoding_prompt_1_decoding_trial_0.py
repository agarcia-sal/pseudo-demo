def checkSimilarity():
    # Read input values for two sets of integers
    firstSet = input()
    secondSet = input()

    # Split the input strings into individual integers
    firstList = firstSet.split()
    secondList = secondSet.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Loop through the integers in both lists
    for index in range(3):
        # Convert string values to integers for comparison
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])

        # Check if the integers are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 

    # If the number of differences is less than 3
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution starts here
checkSimilarity()
