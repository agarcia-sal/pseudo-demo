def doMain():
    # Read two input strings from the user
    firstInput = input()
    secondInput = input()
    
    # Split the input strings into lists of words
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize the difference counter
    differenceCounter = 0 
    
    # Loop through the first three items in both lists
    for index in range(3):
        # Convert the current items from the lists to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check if the values are different
        if firstValue != secondValue:
            # Increment the difference counter
            differenceCounter += 1
            
    # If the count of differences is less than 3, print "YES"
    if differenceCounter < 3:
        print("YES")
    else:
        print("NO")

# Call the main function to execute the program
doMain()
