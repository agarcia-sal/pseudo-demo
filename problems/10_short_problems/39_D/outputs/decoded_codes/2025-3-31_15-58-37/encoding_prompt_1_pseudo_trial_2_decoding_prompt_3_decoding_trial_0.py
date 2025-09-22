def doMain():
    # Get two lines of input from the user
    firstInput = input()
    secondInput = input()
    
    # Split the inputs into separate components
    splitFirstInput = firstInput.split()
    splitSecondInput = secondInput.split()
    
    # Initialize a variable to count the number of differences
    differenceCount = 0 

    # Iterate through the first three elements of both inputs
    for index in range(3):  # Assuming each input has at least 3 elements
        # Convert the current elements to integers
        firstValue = int(splitFirstInput[index])
        secondValue = int(splitSecondInput[index])
        
        # Check if the two values are different
        if firstValue != secondValue:
            # Increment the count of differences
            differenceCount += 1 

    # If the number of differences is less than 3, print "YES", otherwise print "NO"
    if differenceCount < 3:
        print("YES")
    else:
        print("NO")

# Main execution flow
doMain()
