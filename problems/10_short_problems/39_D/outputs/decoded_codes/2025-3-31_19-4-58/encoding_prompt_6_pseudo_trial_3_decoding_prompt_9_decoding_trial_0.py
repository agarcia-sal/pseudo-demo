def doMain():
    # Read inputs from the user
    firstInput = input()  # First input string
    secondInput = input()  # Second input string
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()  # Convert input string to a list of words
    secondList = secondInput.split()  # Convert input string to a list of words
    
    # Initialize a counter for differences
    differenceCount = 0  # Counter for differing values
    
    # Loop through the first three elements of both lists
    for index in range(3):  # Loop from index 0 to 2 (inclusive)
        # Convert the current elements to integers
        firstValue = int(firstList[index])  # Convert to integer
        secondValue = int(secondList[index])  # Convert to integer
        
        # Compare the two values
        if firstValue != secondValue:  # Check if values are different
            # Increment the difference counter if the values are different
            differenceCount += 1  # Increment the counter
    
    # Decide the final output based on the number of differences
    if differenceCount < 3:  # Check if differences are less than 3
        print("YES")  # Output YES if fewer than 3 differences
    else:
        print("NO")  # Output NO if 3 or more differences

# Main program execution
doMain()
