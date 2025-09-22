def doMain():
    # Read two input strings from the user
    firstInput = input()  # First line of input
    secondInput = input()  # Second line of input
    
    # Split the input strings into lists of words
    firstList = firstInput.split()  # Splitting the first input string
    secondList = secondInput.split()  # Splitting the second input string
    
    # Initialize the difference counter
    differenceCounter = 0 
    
    # Loop through the first three items in both lists
    for index in range(3):  # Looping through index 0 to 2
        # Convert the current items from the lists to integers
        firstValue = int(firstList[index])  # Convert to integer from first list
        secondValue = int(secondList[index])  # Convert to integer from second list
        
        # Check if the values are different
        if firstValue != secondValue:  # If values are not equal
            # Increment the difference counter
            differenceCounter += 1  # Incrementing the counter for differences
    
    # If the count of differences is less than 3, print "YES"
    if differenceCounter < 3:  # Checking if differences are less than 3
        print("YES")  # Condition met
    else:
        print("NO")  # Condition not met

# Call the main function to execute the program
doMain()
