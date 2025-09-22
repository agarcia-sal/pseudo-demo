def doMain():
    # Read two lines of input
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize a variable to count the differences
    differenceCount = 0
    
    # Iterate through the first three elements of both lists
    for index in range(3):
        # Convert the string values to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Compare the two values
        if firstValue != secondValue:
            # Increment the count of differences
            differenceCount += 1
            
    # Evaluate the number of differences
    if differenceCount < 3:
        # Print "YES" if differences are fewer than three
        print("YES")
    else:
        # Print "NO" if differences are three or more
        print("NO")

# Execute the main function when the program starts
doMain()


    1 2 3
    1 2 4
    

    5 6 7
    5 6 7
    

    2 2 2
    1 1 1
    

    8 9 10
    8 9 11
    