def doMain():
    # Read user input
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()

    # Initialize a counter for differences
    differenceCount = 0 
    
    # Loop through the first three elements of both lists
    for index in range(3):
        # Convert the current elements to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCount += 1 

    # Check the number of differences and print the result
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")
        
# Execute the main function
doMain()
