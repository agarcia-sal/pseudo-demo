def CompareIntegers():
    # Get two sets of three integers from the user
    firstSet = input()
    secondSet = input()

    # Split the input strings into lists of integers
    firstList = firstSet.split()
    secondList = secondSet.split()

    # Initialize a counter for differences
    differenceCount = 0 

    # Iterate through the first three integers in both lists
    for index in range(3):
        # Convert string values to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 

    # Determine if the count of differences is less than three
    if differenceCount < 3:
        print("YES")  # Indicate that the differences are acceptable
    else:
        print("NO")   # Indicate that there are too many differences

# Main process begins here
CompareIntegers()
