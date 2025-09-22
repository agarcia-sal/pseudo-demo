def doMain():
    # Read two lines of input
    firstLine = input()
    secondLine = input()
    
    # Split the input lines into lists of words
    firstList = firstLine.split()
    secondList = secondLine.split()
    
    # Initialize a counter for differences
    differenceCount = 0
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Only iterate through the first three elements
        # Convert elements to integers for comparison
        valueA = int(firstList[index])
        valueB = int(secondList[index])
        
        # Check if the values are different
        if valueA != valueB:
            # Increment the difference count if values are not equal
            differenceCount += 1
            
    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Start execution of the program
doMain()
