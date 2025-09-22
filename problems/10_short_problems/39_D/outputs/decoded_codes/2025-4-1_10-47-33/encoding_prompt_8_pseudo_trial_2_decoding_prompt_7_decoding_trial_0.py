def compareThreeIntegers():
    # Prompt the user for the first set of integers
    firstInput = input()
    
    # Prompt the user for the second set of integers
    secondInput = input()
    
    # Split the input strings into lists of strings
    firstList = firstInput.split()
    secondList = secondInput.split()
    
    # Initialize the difference counter
    differenceCount = 0
    
    # Loop through the indices 0 to 2 (inclusive) to compare integer values
    for index in range(3):
        # Convert the string values to integers
        firstValue = int(firstList[index])
        secondValue = int(secondList[index])
        
        # Check for inequality and update the difference counter
        if firstValue != secondValue:
            differenceCount += 1
    
    # Check if the number of differences is less than 3
    if differenceCount < 3:
        print("YES")  # Output "YES" if they differ by less than three integers
    else:
        print("NO")   # Output "NO" otherwise

# Execute the function to run the program
compareThreeIntegers()
